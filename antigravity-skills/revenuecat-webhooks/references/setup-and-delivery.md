# RevenueCat Webhook Setup and Delivery

## Configuration
Webhooks are configured in the RevenueCat Dashboard under Project settings -> Integrations -> Webhooks. You can specify:
- Webhook URL (must be HTTPS)
- Authorization header (optional but highly recommended)

## Authorization (Security)
RevenueCat does not use HMAC signatures. Instead, it relies on a shared secret passed via the `Authorization` header.
- **Format:** You define the value in the dashboard (e.g., `Bearer YOUR_SECRET_TOKEN`).
- **Validation:** Your server must check incoming POST requests to ensure `req.headers.authorization` matches the expected token. If it doesn't, return a `401 Unauthorized`.

## Delivery and Retries
- **Response Time:** Your server should process the request quickly and return a `200`, `201`, or `204` status code.
- **Retries:** If RevenueCat receives a non-200 response (or a timeout occurs), it will retry sending the webhook up to 5 times over the course of approximately 24 hours.
- **Order of Events:** RevenueCat does not guarantee the delivery order of webhooks. It is essential to check the `purchased_at_ms` or `updated_at_ms` fields in the payload to ensure you aren't processing an older event over a newer one.
- **Sandbox vs. Production:** Events generated in the sandbox environment will have the `environment` field set to `SANDBOX`. Production events will be set to `PRODUCTION`.