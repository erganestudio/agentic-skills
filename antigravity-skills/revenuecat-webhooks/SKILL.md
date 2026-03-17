---
name: revenuecat-webhooks
description: >
  Expert knowledge on RevenueCat Webhooks for building server-side webhook listeners,
  especially in .NET (ASP.NET Core / C#). Use this skill whenever the user asks about:
  RevenueCat webhooks, in-app purchase events, subscription lifecycle, webhook endpoint
  implementation, handling RevenueCat payloads, .NET webhook listener, C# webhook handler,
  idempotency for webhooks, subscription status sync, INITIAL_PURCHASE / RENEWAL /
  CANCELLATION / EXPIRATION events, or any RevenueCat integration question. Always
  trigger this skill when RevenueCat + webhooks are mentioned together, even if the
  question seems simple.
---

# RevenueCat Webhooks Skill

This skill covers everything needed to understand, implement, and maintain a RevenueCat webhook listener — with a focus on **ASP.NET Core / C# (.NET)** backends.

## Quick Reference

- RevenueCat sends `POST` requests with a JSON body to your HTTPS endpoint
- Your server must return **HTTP 200** within **60 seconds**
- RevenueCat retries up to **5 times** (delays: 5, 10, 20, 40, 80 minutes)
- Always make your handler **idempotent** — deduplication by `event.id`
- Available on the **Pro plan** only

---

## 1. Setup (Dashboard)

1. Go to **Project → Integrations → Webhooks → Add new configuration**
2. Name the webhook, enter your HTTPS URL
3. (Optional) Set an **Authorization header** — RevenueCat sends this with every request; validate it in your handler
4. Choose environment: Production, Sandbox, or Both
5. Optionally filter to specific apps or event types

---

## 2. Payload Structure

Every webhook is a `POST` with `Content-Type: application/json`:

```json
{
  "api_version": "1.0",
  "event": {
    "type": "INITIAL_PURCHASE",
    "id": "UniqueEventID",
    "app_id": "yourAppID",
    "event_timestamp_ms": 1591121855319,
    "app_user_id": "yourCustomerAppUserID",
    "original_app_user_id": "OriginalAppUserID",
    "aliases": ["alias1", "alias2"],
    "product_id": "onemonth_no_trial",
    "entitlement_ids": ["pro_cat"],
    "period_type": "NORMAL",
    "purchased_at_ms": 1591121853000,
    "expiration_at_ms": 1591726653000,
    "store": "APP_STORE",
    "environment": "PRODUCTION",
    "currency": "USD",
    "price": 2.49,
    "price_in_purchased_currency": 2.49,
    "transaction_id": "170000869511114",
    "original_transaction_id": "1530648507000",
    "subscriber_attributes": {}
  }
}
```

For the full field reference, see → `references/fields.md`  
For sample payloads per event type, see → `references/sample-events.md`

---

## 3. All Event Types

| Event | When it fires |
|---|---|
| `TEST` | Manual test from dashboard |
| `INITIAL_PURCHASE` | First subscription purchase |
| `RENEWAL` | Subscription renewed / lapsed user resubscribed |
| `CANCELLATION` | Subscription or non-renewing purchase cancelled/refunded |
| `UNCANCELLATION` | Cancelled subscription re-enabled before expiry |
| `NON_RENEWING_PURCHASE` | One-time purchase (no auto-renew) |
| `SUBSCRIPTION_PAUSED` | Subscription set to pause at period end (Android only) |
| `EXPIRATION` | Subscription expired → revoke access now |
| `BILLING_ISSUE` | Payment charge failed |
| `PRODUCT_CHANGE` | Subscriber changed product/tier |
| `TRANSFER` | Entitlements transferred between user IDs |
| `SUBSCRIPTION_EXTENDED` | Expiration date pushed further into future |
| `TEMPORARY_ENTITLEMENT_GRANT` | Short-term access granted during store outage |
| `REFUND_REVERSED` | A previous refund was reversed (App Store only) |
| `INVOICE_ISSUANCE` | Invoice created (Web Billing only) |
| `VIRTUAL_CURRENCY_TRANSACTION` | Virtual currency balance adjusted |
| `EXPERIMENT_ENROLLMENT` | Customer enrolled in an A/B experiment |

**Key access-control rules:**
- Grant access on: `INITIAL_PURCHASE`, `RENEWAL`, `UNCANCELLATION`, `SUBSCRIPTION_EXTENDED`, `TEMPORARY_ENTITLEMENT_GRANT`
- Revoke access on: `EXPIRATION` only (NOT on `CANCELLATION` or `SUBSCRIPTION_PAUSED`)
- Use `expiration_at_ms` to determine if a subscription is still active

---

## 4. .NET Implementation

### 4a. Models (C#)

```csharp
public class RevenueCatWebhookPayload
{
    [JsonPropertyName("api_version")]
    public string ApiVersion { get; set; } = string.Empty;

    [JsonPropertyName("event")]
    public RevenueCatEvent Event { get; set; } = new();
}

public class RevenueCatEvent
{
    [JsonPropertyName("type")]
    public string Type { get; set; } = string.Empty;

    [JsonPropertyName("id")]
    public string Id { get; set; } = string.Empty;

    [JsonPropertyName("app_id")]
    public string? AppId { get; set; }

    [JsonPropertyName("event_timestamp_ms")]
    public long EventTimestampMs { get; set; }

    [JsonPropertyName("app_user_id")]
    public string? AppUserId { get; set; }

    [JsonPropertyName("original_app_user_id")]
    public string? OriginalAppUserId { get; set; }

    [JsonPropertyName("aliases")]
    public List<string> Aliases { get; set; } = new();

    [JsonPropertyName("product_id")]
    public string? ProductId { get; set; }

    [JsonPropertyName("entitlement_ids")]
    public List<string>? EntitlementIds { get; set; }

    [JsonPropertyName("period_type")]
    public string? PeriodType { get; set; }

    [JsonPropertyName("purchased_at_ms")]
    public long? PurchasedAtMs { get; set; }

    [JsonPropertyName("expiration_at_ms")]
    public long? ExpirationAtMs { get; set; }

    [JsonPropertyName("store")]
    public string? Store { get; set; }

    [JsonPropertyName("environment")]
    public string? Environment { get; set; }

    [JsonPropertyName("currency")]
    public string? Currency { get; set; }

    [JsonPropertyName("price")]
    public double? Price { get; set; }

    [JsonPropertyName("price_in_purchased_currency")]
    public double? PriceInPurchasedCurrency { get; set; }

    [JsonPropertyName("transaction_id")]
    public string? TransactionId { get; set; }

    [JsonPropertyName("original_transaction_id")]
    public string? OriginalTransactionId { get; set; }

    [JsonPropertyName("cancel_reason")]
    public string? CancelReason { get; set; }

    [JsonPropertyName("expiration_reason")]
    public string? ExpirationReason { get; set; }

    [JsonPropertyName("is_trial_conversion")]
    public bool? IsTrialConversion { get; set; }

    [JsonPropertyName("new_product_id")]
    public string? NewProductId { get; set; }

    [JsonPropertyName("subscriber_attributes")]
    public Dictionary<string, SubscriberAttribute>? SubscriberAttributes { get; set; }

    [JsonPropertyName("transferred_from")]
    public List<string>? TransferredFrom { get; set; }

    [JsonPropertyName("transferred_to")]
    public List<string>? TransferredTo { get; set; }

    [JsonPropertyName("is_family_share")]
    public bool? IsFamilyShare { get; set; }

    [JsonPropertyName("country_code")]
    public string? CountryCode { get; set; }

    [JsonPropertyName("renewal_number")]
    public int? RenewalNumber { get; set; }
}

public class SubscriberAttribute
{
    [JsonPropertyName("value")]
    public string? Value { get; set; }

    [JsonPropertyName("updated_at_ms")]
    public long UpdatedAtMs { get; set; }
}

// Strongly-typed event type constants
public static class RevenueCatEventType
{
    public const string Test = "TEST";
    public const string InitialPurchase = "INITIAL_PURCHASE";
    public const string Renewal = "RENEWAL";
    public const string Cancellation = "CANCELLATION";
    public const string Uncancellation = "UNCANCELLATION";
    public const string NonRenewingPurchase = "NON_RENEWING_PURCHASE";
    public const string SubscriptionPaused = "SUBSCRIPTION_PAUSED";
    public const string Expiration = "EXPIRATION";
    public const string BillingIssue = "BILLING_ISSUE";
    public const string ProductChange = "PRODUCT_CHANGE";
    public const string Transfer = "TRANSFER";
    public const string SubscriptionExtended = "SUBSCRIPTION_EXTENDED";
    public const string TemporaryEntitlementGrant = "TEMPORARY_ENTITLEMENT_GRANT";
    public const string RefundReversed = "REFUND_REVERSED";
    public const string InvoiceIssuance = "INVOICE_ISSUANCE";
    public const string VirtualCurrencyTransaction = "VIRTUAL_CURRENCY_TRANSACTION";
    public const string ExperimentEnrollment = "EXPERIMENT_ENROLLMENT";
}
```

### 4b. Controller / Endpoint

```csharp
[ApiController]
[Route("webhooks")]
public class RevenueCatWebhookController : ControllerBase
{
    private readonly IRevenueCatWebhookService _webhookService;
    private readonly IConfiguration _configuration;
    private readonly ILogger<RevenueCatWebhookController> _logger;

    public RevenueCatWebhookController(
        IRevenueCatWebhookService webhookService,
        IConfiguration configuration,
        ILogger<RevenueCatWebhookController> logger)
    {
        _webhookService = webhookService;
        _configuration = configuration;
        _logger = logger;
    }

    [HttpPost("revenuecat")]
    public async Task<IActionResult> HandleWebhook(
        [FromBody] RevenueCatWebhookPayload payload,
        CancellationToken cancellationToken)
    {
        // 1. Validate authorization header
        if (!ValidateAuthorization())
            return Unauthorized();

        // 2. Respond fast — queue for background processing
        _ = Task.Run(() => _webhookService.ProcessAsync(payload, cancellationToken), cancellationToken);

        // 3. Always return 200 quickly
        return Ok();
    }

    private bool ValidateAuthorization()
    {
        var expectedToken = _configuration["RevenueCat:WebhookAuthorizationHeader"];
        if (string.IsNullOrEmpty(expectedToken))
            return true; // No auth configured — skip validation

        if (!Request.Headers.TryGetValue("Authorization", out var receivedToken))
            return false;

        return receivedToken == expectedToken;
    }
}
```

### 4c. Service with Idempotency + Event Routing

```csharp
public interface IRevenueCatWebhookService
{
    Task ProcessAsync(RevenueCatWebhookPayload payload, CancellationToken ct);
}

public class RevenueCatWebhookService : IRevenueCatWebhookService
{
    private readonly ISubscriptionRepository _subscriptions;
    private readonly IProcessedEventRepository _processedEvents;
    private readonly ILogger<RevenueCatWebhookService> _logger;

    public RevenueCatWebhookService(
        ISubscriptionRepository subscriptions,
        IProcessedEventRepository processedEvents,
        ILogger<RevenueCatWebhookService> logger)
    {
        _subscriptions = subscriptions;
        _processedEvents = processedEvents;
        _logger = logger;
    }

    public async Task ProcessAsync(RevenueCatWebhookPayload payload, CancellationToken ct)
    {
        var evt = payload.Event;

        // Idempotency check — skip duplicate events
        if (await _processedEvents.HasBeenProcessedAsync(evt.Id, ct))
        {
            _logger.LogInformation("Duplicate webhook event {EventId} — skipped", evt.Id);
            return;
        }

        _logger.LogInformation("Processing RevenueCat event {Type} for user {UserId}",
            evt.Type, evt.AppUserId);

        try
        {
            await (evt.Type switch
            {
                RevenueCatEventType.InitialPurchase => HandleInitialPurchaseAsync(evt, ct),
                RevenueCatEventType.Renewal => HandleRenewalAsync(evt, ct),
                RevenueCatEventType.Cancellation => HandleCancellationAsync(evt, ct),
                RevenueCatEventType.Uncancellation => HandleUncancellationAsync(evt, ct),
                RevenueCatEventType.Expiration => HandleExpirationAsync(evt, ct),
                RevenueCatEventType.BillingIssue => HandleBillingIssueAsync(evt, ct),
                RevenueCatEventType.ProductChange => HandleProductChangeAsync(evt, ct),
                RevenueCatEventType.NonRenewingPurchase => HandleNonRenewingPurchaseAsync(evt, ct),
                RevenueCatEventType.Transfer => HandleTransferAsync(evt, ct),
                RevenueCatEventType.SubscriptionExtended => HandleSubscriptionExtendedAsync(evt, ct),
                RevenueCatEventType.TemporaryEntitlementGrant => HandleTemporaryEntitlementAsync(evt, ct),
                RevenueCatEventType.Test => HandleTestAsync(evt, ct),
                _ => HandleUnknownAsync(evt, ct)
            });

            // Mark as processed only after successful handling
            await _processedEvents.MarkProcessedAsync(evt.Id, ct);
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Failed to process event {EventId} of type {Type}", evt.Id, evt.Type);
            throw;
        }
    }

    private async Task HandleInitialPurchaseAsync(RevenueCatEvent evt, CancellationToken ct)
    {
        // Grant subscription/entitlements
        var expiresAt = evt.ExpirationAtMs.HasValue
            ? DateTimeOffset.FromUnixTimeMilliseconds(evt.ExpirationAtMs.Value)
            : (DateTimeOffset?)null;

        await _subscriptions.GrantAccessAsync(
            userId: evt.OriginalAppUserId ?? evt.AppUserId!,
            productId: evt.ProductId!,
            entitlementIds: evt.EntitlementIds ?? new(),
            expiresAt: expiresAt,
            transactionId: evt.TransactionId,
            cancellationToken: ct);
    }

    private async Task HandleRenewalAsync(RevenueCatEvent evt, CancellationToken ct)
    {
        // Extend/refresh subscription expiry
        var expiresAt = evt.ExpirationAtMs.HasValue
            ? DateTimeOffset.FromUnixTimeMilliseconds(evt.ExpirationAtMs.Value)
            : (DateTimeOffset?)null;

        await _subscriptions.RenewAccessAsync(
            userId: evt.OriginalAppUserId ?? evt.AppUserId!,
            productId: evt.ProductId!,
            entitlementIds: evt.EntitlementIds ?? new(),
            expiresAt: expiresAt,
            isTrialConversion: evt.IsTrialConversion ?? false,
            cancellationToken: ct);
    }

    private async Task HandleCancellationAsync(RevenueCatEvent evt, CancellationToken ct)
    {
        // Mark as cancelled — do NOT revoke access yet!
        // Access is revoked on EXPIRATION event.
        await _subscriptions.MarkCancelledAsync(
            userId: evt.OriginalAppUserId ?? evt.AppUserId!,
            reason: evt.CancelReason,
            cancellationToken: ct);
    }

    private async Task HandleUncancellationAsync(RevenueCatEvent evt, CancellationToken ct)
    {
        // Re-enable — user resubscribed before expiry
        await _subscriptions.MarkActiveAsync(
            userId: evt.OriginalAppUserId ?? evt.AppUserId!,
            cancellationToken: ct);
    }

    private async Task HandleExpirationAsync(RevenueCatEvent evt, CancellationToken ct)
    {
        // REVOKE ACCESS HERE — this is the definitive "access ends" event
        await _subscriptions.RevokeAccessAsync(
            userId: evt.OriginalAppUserId ?? evt.AppUserId!,
            reason: evt.ExpirationReason,
            cancellationToken: ct);
    }

    private async Task HandleBillingIssueAsync(RevenueCatEvent evt, CancellationToken ct)
    {
        // Notify user about payment failure — do NOT revoke access
        await _subscriptions.RecordBillingIssueAsync(
            userId: evt.OriginalAppUserId ?? evt.AppUserId!,
            gracePeriodEndsAt: evt.ExpirationAtMs.HasValue
                ? DateTimeOffset.FromUnixTimeMilliseconds(evt.ExpirationAtMs.Value)
                : null,
            cancellationToken: ct);
    }

    private async Task HandleProductChangeAsync(RevenueCatEvent evt, CancellationToken ct)
    {
        await _subscriptions.UpdateProductAsync(
            userId: evt.OriginalAppUserId ?? evt.AppUserId!,
            oldProductId: evt.ProductId!,
            newProductId: evt.NewProductId,
            cancellationToken: ct);
    }

    private async Task HandleNonRenewingPurchaseAsync(RevenueCatEvent evt, CancellationToken ct)
    {
        await _subscriptions.RecordOneTimePurchaseAsync(
            userId: evt.OriginalAppUserId ?? evt.AppUserId!,
            productId: evt.ProductId!,
            entitlementIds: evt.EntitlementIds ?? new(),
            cancellationToken: ct);
    }

    private async Task HandleTransferAsync(RevenueCatEvent evt, CancellationToken ct)
    {
        if (evt.TransferredFrom != null && evt.TransferredTo != null)
        {
            await _subscriptions.TransferEntitlementsAsync(
                fromUserIds: evt.TransferredFrom,
                toUserIds: evt.TransferredTo,
                cancellationToken: ct);
        }
    }

    private async Task HandleSubscriptionExtendedAsync(RevenueCatEvent evt, CancellationToken ct)
    {
        var newExpiry = evt.ExpirationAtMs.HasValue
            ? DateTimeOffset.FromUnixTimeMilliseconds(evt.ExpirationAtMs.Value)
            : (DateTimeOffset?)null;

        await _subscriptions.ExtendSubscriptionAsync(
            userId: evt.OriginalAppUserId ?? evt.AppUserId!,
            newExpiresAt: newExpiry,
            cancellationToken: ct);
    }

    private async Task HandleTemporaryEntitlementAsync(RevenueCatEvent evt, CancellationToken ct)
    {
        // Short-term access during store outage — max 24 hours
        var expiresAt = evt.ExpirationAtMs.HasValue
            ? DateTimeOffset.FromUnixTimeMilliseconds(evt.ExpirationAtMs.Value)
            : DateTimeOffset.UtcNow.AddHours(24);

        await _subscriptions.GrantTemporaryAccessAsync(
            userId: evt.AppUserId!,
            expiresAt: expiresAt,
            cancellationToken: ct);
    }

    private Task HandleTestAsync(RevenueCatEvent evt, CancellationToken ct)
    {
        _logger.LogInformation("RevenueCat TEST webhook received successfully");
        return Task.CompletedTask;
    }

    private Task HandleUnknownAsync(RevenueCatEvent evt, CancellationToken ct)
    {
        _logger.LogWarning("Unhandled RevenueCat event type: {Type}", evt.Type);
        return Task.CompletedTask;
    }
}
```

### 4d. Program.cs / DI Registration

```csharp
builder.Services.AddScoped<IRevenueCatWebhookService, RevenueCatWebhookService>();
builder.Services.AddScoped<ISubscriptionRepository, SubscriptionRepository>();
builder.Services.AddScoped<IProcessedEventRepository, ProcessedEventRepository>();
```

### 4e. appsettings.json

```json
{
  "RevenueCat": {
    "WebhookAuthorizationHeader": "YOUR_SECRET_HEADER_VALUE_FROM_DASHBOARD"
  }
}
```

---

## 5. Best Practices Checklist

| Practice | Details |
|---|---|
| **Respond in < 60s** | Return 200 immediately; process in background |
| **Idempotency** | Store processed `event.id` values; skip duplicates |
| **Validate auth header** | Check `Authorization` header matches dashboard secret |
| **Use `EXPIRATION` to revoke** | Never revoke on `CANCELLATION` or `SUBSCRIPTION_PAUSED` |
| **Look up by `original_app_user_id`** | Also check `aliases` array for alias matching |
| **Handle new fields gracefully** | RevenueCat may add fields — use flexible deserialization |
| **Handle new event types** | Log and ignore unknown `type` values |
| **Sandbox vs Production** | Filter by `environment` field; use separate webhook configs for each |
| **Delivery delays** | Most events: 5–60 seconds. Cancellation events: up to 2 hours |
| **At-least-once delivery** | RevenueCat may send the same event more than once |

---

## 6. User Identification

When looking up a user from a webhook, always search by **both**:
1. `original_app_user_id` — the canonical user ID
2. `aliases` array — all historical user IDs ever used

```csharp
// Example lookup
var userId = evt.OriginalAppUserId;
var allIds = new List<string> { userId ?? "" }
    .Concat(evt.Aliases ?? new())
    .Where(id => !string.IsNullOrEmpty(id))
    .Distinct()
    .ToList();
```

---

## 7. Syncing Subscription Status (Recommended Pattern)

Rather than writing complex logic for each event type, the recommended approach is:

> After receiving **any** webhook, call the `GET /v1/subscribers/{app_user_id}` REST API endpoint to get the full, canonical subscription state.

This avoids edge cases and keeps your database always consistent with RevenueCat's source of truth.

---

## 8. Testing

- Use **RevenueCat Dashboard → Webhooks → Send Test Event** to verify your endpoint
- Use **sandbox purchases** on device (events have `environment: "SANDBOX"`)
- Failed/retrying events can be manually retried from the dashboard
- When testing locally, use a tunnel like `ngrok` to expose your endpoint

---

## Reference Files

- `references/fields.md` — Complete field-by-field reference table
- `references/sample-events.md` — Full JSON sample payloads for all event types