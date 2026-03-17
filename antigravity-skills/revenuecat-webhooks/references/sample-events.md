# RevenueCat Sample Webhook Payloads

## INITIAL_PURCHASE

```json
{
  "event": {
    "event_timestamp_ms": 1658726378679,
    "product_id": "com.subscription.weekly",
    "period_type": "NORMAL",
    "purchased_at_ms": 1658726374000,
    "expiration_at_ms": 1659331174000,
    "environment": "PRODUCTION",
    "entitlement_ids": ["pro"],
    "transaction_id": "123456789012345",
    "original_transaction_id": "123456789012345",
    "is_family_share": false,
    "country_code": "US",
    "app_user_id": "1234567890",
    "aliases": ["$RCAnonymousID:8069238d6049ce87cc529853916d624c"],
    "original_app_user_id": "$RCAnonymousID:87c6049c58069238dce29853916d624c",
    "currency": "USD",
    "price": 4.99,
    "price_in_purchased_currency": 4.99,
    "store": "APP_STORE",
    "tax_percentage": 0.0,
    "commission_percentage": 0.3,
    "type": "INITIAL_PURCHASE",
    "id": "12345678-1234-1234-1234-123456789012",
    "app_id": "1234567890"
  },
  "api_version": "1.0"
}
```

## RENEWAL

```json
{
  "event": {
    "event_timestamp_ms": 1658726405017,
    "product_id": "com.subscription.weekly",
    "period_type": "NORMAL",
    "purchased_at_ms": 1658755132000,
    "expiration_at_ms": 1659359932000,
    "environment": "PRODUCTION",
    "entitlement_ids": ["pro"],
    "transaction_id": "123456789012345",
    "original_transaction_id": "123456789012345",
    "is_family_share": false,
    "country_code": "DE",
    "app_user_id": "1234567890",
    "original_app_user_id": "$RCAnonymousID:87c6049c58069238dce29853916d624c",
    "currency": "EUR",
    "is_trial_conversion": false,
    "price": 8.14,
    "price_in_purchased_currency": 7.99,
    "store": "APP_STORE",
    "tax_percentage": 0.0,
    "commission_percentage": 0.3,
    "type": "RENEWAL",
    "id": "12345678-1234-1234-1234-123456789012",
    "app_id": "1234567890"
  },
  "api_version": "1.0"
}
```

## CANCELLATION (user unsubscribed)

```json
{
  "event": {
    "event_timestamp_ms": 1601337615995,
    "product_id": "com.revenuecat.myapp.weekly",
    "period_type": "NORMAL",
    "purchased_at_ms": 1601417766000,
    "expiration_at_ms": 1602022566000,
    "environment": "PRODUCTION",
    "entitlement_ids": ["pro"],
    "transaction_id": "100000000000002",
    "original_transaction_id": "100000000000000",
    "app_user_id": "$RCAnonymousID:12345678-1234-1234-1234-123456789123",
    "aliases": [
      "$RCAnonymousID:12345678-1234-ABCD-1234-123456789123",
      "user_1234"
    ],
    "original_app_user_id": "$RCAnonymousID:12345678-1234-ABCD-1234-123456789123",
    "cancel_reason": "UNSUBSCRIBE",
    "currency": "USD",
    "price": 0.0,
    "store": "APP_STORE",
    "tax_percentage": 0.0,
    "commission_percentage": 0.3,
    "type": "CANCELLATION",
    "id": "12345678-ABCD-1234-ABCD-12345678912"
  },
  "api_version": "1.0"
}
```

## CANCELLATION (refund — negative price)

```json
{
  "event": {
    "event_timestamp_ms": 1601337615995,
    "product_id": "com.revenuecat.myapp.monthly",
    "period_type": "NORMAL",
    "cancel_reason": "CUSTOMER_SUPPORT",
    "currency": "USD",
    "price": -9.99,
    "price_in_purchased_currency": -9.99,
    "store": "APP_STORE",
    "type": "CANCELLATION",
    "id": "12345678-1234-1234-1234-12345678912"
  },
  "api_version": "1.0"
}
```

## EXPIRATION

```json
{
  "event": {
    "event_timestamp_ms": 1697451462232,
    "product_id": "com.subscription.weekly",
    "period_type": "NORMAL",
    "expiration_at_ms": 1697451423000,
    "environment": "PRODUCTION",
    "entitlement_ids": ["pro"],
    "app_user_id": "1234567890",
    "expiration_reason": "UNSUBSCRIBE",
    "currency": "USD",
    "price": 0.0,
    "store": "APP_STORE",
    "type": "EXPIRATION",
    "id": "12345678-1234-1234-1234-123456789012"
  },
  "api_version": "1.0"
}
```

## UNCANCELLATION

```json
{
  "event": {
    "event_timestamp_ms": 1663982135337,
    "product_id": "com.subscription.monthly",
    "expiration_at_ms": 1665235092000,
    "environment": "PRODUCTION",
    "entitlement_ids": ["plus"],
    "app_user_id": "1234567890",
    "store": "APP_STORE",
    "type": "UNCANCELLATION",
    "id": "12345678-1234-1234-1234-123456789012"
  },
  "api_version": "1.0"
}
```

## BILLING_ISSUE

```json
{
  "event": {
    "event_timestamp_ms": 1601337601013,
    "product_id": "com.revenuecat.myapp.monthly",
    "period_type": "NORMAL",
    "entitlement_ids": ["pro"],
    "app_user_id": "$RCAnonymousID:12345678-1234-1234-1234-123456789123",
    "original_app_user_id": "$RCAnonymousID:12345678-1234-1234-1234-123456789123",
    "store": "APP_STORE",
    "type": "BILLING_ISSUE",
    "id": "12345678-1234-1234-1234-12345678912"
  },
  "api_version": "1.0"
}
```

## NON_RENEWING_PURCHASE (one-time)

```json
{
  "event": {
    "event_timestamp_ms": 1658726522314,
    "product_id": "2100_tokens",
    "period_type": "NORMAL",
    "purchased_at_ms": 1658726519000,
    "expiration_at_ms": null,
    "environment": "PRODUCTION",
    "entitlement_ids": ["pro"],
    "country_code": "CA",
    "app_user_id": "1234567890",
    "currency": "CAD",
    "price": 25.487,
    "price_in_purchased_currency": 32.99,
    "store": "APP_STORE",
    "commission_percentage": 0.15,
    "type": "NON_RENEWING_PURCHASE",
    "id": "12345678-1234-1234-1234-123456789012"
  },
  "api_version": "1.0"
}
```

## SUBSCRIPTION_PAUSED (Android only)

```json
{
  "event": {
    "event_timestamp_ms": 1652796516000,
    "product_id": "premium",
    "auto_resume_at_ms": 1657951448845,
    "environment": "PRODUCTION",
    "entitlement_ids": ["Premium1"],
    "app_user_id": "1234567890",
    "store": "PLAY_STORE",
    "type": "SUBSCRIPTION_PAUSED",
    "id": "12345678-1234-1234-1234-123456789012"
  },
  "api_version": "1.0"
}
```

## TRANSFER

```json
{
  "event": {
    "app_id": "1234567890",
    "event_timestamp_ms": 78789789798798,
    "id": "CD489E0E-5D52-4E03-966B-A7F17788E432",
    "store": "APP_STORE",
    "transferred_from": ["00005A1C-6091-4F81-BE77-F0A83A271AB6"],
    "transferred_to": ["4BEDB450-8EF2-11E9-B475-0800200C9A66"],
    "type": "TRANSFER",
    "environment": "PRODUCTION"
  },
  "api_version": "1.0"
}
```

## PRODUCT_CHANGE

```json
{
  "event": {
    "event_timestamp_ms": 1601338594769,
    "product_id": "com.revenuecat.myapp.monthly",
    "new_product_id": "com.revenuecat.myapp.yearly",
    "environment": "PRODUCTION",
    "entitlement_ids": ["subscription"],
    "app_user_id": "$RCAnonymousID:12345678-1234-1234-1234-123456789123",
    "original_app_user_id": "$RCAnonymousID:12345678-1234-1234-1234-123456789123",
    "store": "PLAY_STORE",
    "type": "PRODUCT_CHANGE",
    "id": "12345678-1234-1234-1234-12345678912"
  },
  "api_version": "1.0"
}
```

## SUBSCRIPTION_EXTENDED

```json
{
  "event": {
    "event_timestamp_ms": 1697451462232,
    "product_id": "com.subscription.weekly",
    "expiration_at_ms": 1697451423000,
    "environment": "PRODUCTION",
    "entitlement_ids": ["pro"],
    "app_user_id": "1234567890",
    "store": "APP_STORE",
    "type": "SUBSCRIPTION_EXTENDED",
    "id": "12345678-1234-1234-1234-123456789012"
  },
  "api_version": "1.0"
}
```

## REFUND_REVERSED

```json
{
  "event": {
    "product_id": "com.subscription.weekly",
    "app_user_id": "1234567890",
    "price": 5.0,
    "renewal_number": 3,
    "store": "APP_STORE",
    "type": "REFUND_REVERSED",
    "id": "12345678-1234-1234-1234-123456789012"
  },
  "api_version": "1.0"
}
```

## TEMPORARY_ENTITLEMENT_GRANT

```json
{
  "event": {
    "event_timestamp_ms": 1744824815307,
    "app_user_id": "41234567890",
    "store": "APP_STORE",
    "type": "TEMPORARY_ENTITLEMENT_GRANT",
    "id": "12345678-1234-1234-1234-123456789012",
    "app_id": "1234567890"
  },
  "api_version": "1.0"
}
```

## Trial Started (INITIAL_PURCHASE with period_type TRIAL)

```json
{
  "event": {
    "product_id": "com.subscription.yearly",
    "period_type": "TRIAL",
    "purchased_at_ms": 1658726358573,
    "expiration_at_ms": 1658992117958,
    "environment": "PRODUCTION",
    "entitlement_ids": ["pro"],
    "price": 0,
    "store": "PLAY_STORE",
    "type": "INITIAL_PURCHASE",
    "id": "12345678-1234-1234-1234-123456789012"
  },
  "api_version": "1.0"
}
```

## INVOICE_ISSUANCE (Web Billing only)

```json
{
  "event": {
    "event_timestamp_ms": 1745004447300,
    "product_id": "com.subscription.monthly",
    "environment": "PRODUCTION",
    "app_user_id": "41234567890",
    "currency": "USD",
    "price_in_purchased_currency": 9.0,
    "store": "RC_BILLING",
    "type": "INVOICE_ISSUANCE",
    "id": "12345678-1234-1234-1234-123456789012"
  },
  "api_version": "1.0"
}
```

## VIRTUAL_CURRENCY_TRANSACTION

```json
{
  "event": {
    "adjustments": [
      {
        "amount": 100,
        "currency": {
          "code": "CRD",
          "description": "The main currency unit",
          "name": "Credits"
        }
      }
    ],
    "app_user_id": "1234567890",
    "product_id": "1M_100credits",
    "source": "in_app_purchase",
    "store": "APP_STORE",
    "virtual_currency_transaction_id": "vatx123456789012345",
    "type": "VIRTUAL_CURRENCY_TRANSACTION",
    "id": "12345678-1234-1234-1234-123456789012"
  },
  "api_version": "1.0"
}
```

## EXPERIMENT_ENROLLMENT

```json
{
  "event": {
    "event_timestamp_ms": 1658726378679,
    "app_user_id": "$RCAnonymousID:12345678-1234-1234-1234-123456789123",
    "experiment_id": "prexpca1234abcd",
    "experiment_variant": "b",
    "offering_id": "experiment_offering_b",
    "experiment_enrolled_at_ms": 1658726378679,
    "type": "EXPERIMENT_ENROLLMENT",
    "id": "12345678-1234-1234-1234-123456789012"
  },
  "api_version": "1.0"
}
```
