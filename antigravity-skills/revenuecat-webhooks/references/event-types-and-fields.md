# Event Types and Fields

Every webhook request contains a JSON body with an `api_version` and an `event` object.

## Core Event Types (`event.type`)
1. `INITIAL_PURCHASE`: A new subscription has been purchased.
2. `RENEWAL`: An existing subscription has been renewed.
3. `PRODUCT_CHANGE`: A user changed from one subscription product to another (upgrade/downgrade).
4. `CANCELLATION`: A user turned off auto-renew. (The subscription is still active until the expiration date).
5. `UNCANCELLATION`: A user turned auto-renew back on before the subscription expired.
6. `BILLING_ISSUE`: There was a billing issue when trying to renew a subscription.
7. `SUBSCRIBER_ALIAS`: A user's App User ID was changed or merged.
8. `SUBSCRIPTION_PAUSED` / `SUBSCRIPTION_EXTENDED` / `EXPIRATION`

## Standard JSON Payload Structure
Below is the standard schema of the `event` object you will receive:

```json
{
  "api_version": "1.0",
  "event": {
    "id": "A-UUID-V4-STRING",
    "type": "INITIAL_PURCHASE",
    "app_user_id": "user_12345",
    "original_app_user_id": "user_12345",
    "aliases": ["user_12345"],
    "product_id": "com.app.monthly",
    "entitlement_ids": ["pro_access"],
    "period_type": "NORMAL",
    "purchased_at_ms": 1614556800000,
    "expiration_at_ms": 1617235200000,
    "environment": "PRODUCTION",
    "store": "APP_STORE",
    "currency": "USD",
    "price": 9.99,
    "price_in_purchased_currency": 9.99,
    "subscriber_attributes": {
      "$email": {
        "value": "user@example.com",
        "updated_at_ms": 1614556800000
      }
    }
  }
}