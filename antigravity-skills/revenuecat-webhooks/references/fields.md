# RevenueCat Webhook Fields Reference

## Common Fields (all events)

| Field                   | Type          | Description                                                                                    |
| ----------------------- | ------------- | ---------------------------------------------------------------------------------------------- |
| `type`                  | String        | Event type (see event types table in SKILL.md)                                                 |
| `id`                    | String        | **Unique event ID** — use for idempotency                                                      |
| `app_id`                | String        | App identifier within the project. Not present when store is `PROMOTIONAL`                     |
| `event_timestamp_ms`    | Integer       | When the event was generated (Unix ms). Same on retries                                        |
| `app_user_id`           | String        | Last seen user ID. Not present on `TRANSFER` events                                            |
| `original_app_user_id`  | String        | First ever user ID for this subscriber                                                         |
| `aliases`               | Array[String] | All user IDs ever used by this subscriber                                                      |
| `subscriber_attributes` | Map           | Key → `{ value, updated_at_ms }` map of custom attributes                                      |
| `experiments`           | Array         | Experiments subscriber is enrolled in: `experiment_id`, `experiment_variant`, `enrolled_at_ms` |

## Subscription Lifecycle Fields

| Field                           | Type          | Description                                                                                                                 | Nullable                    |
| ------------------------------- | ------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------- |
| `product_id`                    | String        | Product identifier. For Google Play post-Feb 2023: `<sub_id>:<base_plan_id>`                                                | No                          |
| `entitlement_ids`               | Array[String] | Entitlement identifiers granted                                                                                             | Yes (if product not mapped) |
| `entitlement_id`                | String        | **Deprecated** — use `entitlement_ids`                                                                                      | Deprecated                  |
| `period_type`                   | String        | `TRIAL`, `INTRO`, `NORMAL`, `PROMOTIONAL`, `PREPAID`                                                                        | No                          |
| `purchased_at_ms`               | Integer       | Transaction purchase time (Unix ms)                                                                                         | No                          |
| `expiration_at_ms`              | Integer       | Transaction expiration (Unix ms). Use to check if active                                                                    | Yes (non-subscription)      |
| `grace_period_expiration_at_ms` | Integer       | Grace period end for billing issues (Unix ms)                                                                               | Yes                         |
| `auto_resume_at_ms`             | Integer       | When paused Android sub resumes (Unix ms)                                                                                   | Yes                         |
| `store`                         | String        | `AMAZON`, `APP_STORE`, `MAC_APP_STORE`, `PADDLE`, `PLAY_STORE`, `PROMOTIONAL`, `RC_BILLING`, `ROKU`, `STRIPE`, `TEST_STORE` | No                          |
| `environment`                   | String        | `SANDBOX` or `PRODUCTION`                                                                                                   | No                          |
| `is_trial_conversion`           | Boolean       | Only on `RENEWAL` — whether prior was a free trial                                                                          | RENEWAL only                |
| `cancel_reason`                 | String        | Only on `CANCELLATION`. See cancellation reasons                                                                            | CANCELLATION only           |
| `expiration_reason`             | String        | Only on `EXPIRATION`. See cancellation reasons                                                                              | EXPIRATION only             |
| `new_product_id`                | String        | New product ID on plan change (Play Store DEFERRED mode / App Store)                                                        | PRODUCT_CHANGE only         |
| `presented_offering_id`         | String        | Offering shown to user at purchase. Can be null for old purchases                                                           | Yes                         |
| `price`                         | Double        | USD price. 0 for trials. Negative for refunds                                                                               | Yes                         |
| `currency`                      | String        | ISO 4217 currency code of purchase (e.g. `USD`, `EUR`)                                                                      | Yes                         |
| `price_in_purchased_currency`   | Double        | Price in local currency                                                                                                     | Yes                         |
| `tax_percentage`                | Double        | Estimated tax % deducted                                                                                                    | Yes                         |
| `commission_percentage`         | Double        | Estimated store commission % deducted                                                                                       | Yes                         |
| `takehome_percentage`           | Double        | **DEPRECATED** — use tax_percentage + commission_percentage instead                                                         | Deprecated                  |
| `transaction_id`                | String        | Store transaction ID                                                                                                        | No                          |
| `original_transaction_id`       | String        | Original transaction ID in subscription chain                                                                               | No                          |
| `is_family_share`               | Boolean       | True if shared via Apple Family Sharing                                                                                     | No                          |
| `transferred_from`              | Array[String] | Only on `TRANSFER` — source user IDs                                                                                        | TRANSFER only               |
| `transferred_to`                | Array[String] | Only on `TRANSFER` — destination user IDs                                                                                   | TRANSFER only               |
| `country_code`                  | String        | ISO 3166 2-letter code (e.g. `US`, `DE`)                                                                                    | Yes                         |
| `offer_code`                    | String        | Offer/promo code redeemed. Null if none                                                                                     | Yes                         |
| `renewal_number`                | Integer       | Number of renewals so far. Starts at 1                                                                                      | Yes                         |

## Cancellation and Expiration Reasons

| Reason                | Description                            | Stores                             |
| --------------------- | -------------------------------------- | ---------------------------------- |
| `UNSUBSCRIBE`         | User cancelled voluntarily             | App Store, Play Store, Amazon, Web |
| `BILLING_ERROR`       | Payment failed                         | App Store, Play Store, Amazon      |
| `DEVELOPER_INITIATED` | Developer cancelled                    | App Store, Play Store, Promo       |
| `PRICE_INCREASE`      | User rejected price increase           | App Store, Play Store              |
| `CUSTOMER_SUPPORT`    | Refund via support                     | App Store, Play Store, Amazon, Web |
| `UNKNOWN`             | Apple didn't provide reason            | App Store                          |
| `SUBSCRIPTION_PAUSED` | Expired due to pause (EXPIRATION only) | Play Store                         |

## Virtual Currency Transaction Fields

| Field                                | Type    | Description                          |
| ------------------------------------ | ------- | ------------------------------------ |
| `adjustments`                        | Array   | Array of currency adjustments        |
| `adjustments[].amount`               | Integer | Positive = added, Negative = removed |
| `adjustments[].currency.code`        | String  | Virtual currency identifier          |
| `adjustments[].currency.name`        | String  | Display name                         |
| `adjustments[].currency.description` | String  | Description                          |
| `product_display_name`               | String  | Display name of triggering product   |
| `purchase_environment`               | String  | `SANDBOX` or `PRODUCTION`            |
| `source`                             | String  | `in_app_purchase` or `admin_api`     |
| `virtual_currency_transaction_id`    | String  | Unique ID for this transaction       |

## Experiment Enrollment Fields

| Field                | Type    | Description                |
| -------------------- | ------- | -------------------------- |
| `experiment_id`      | String  | ID of the experiment       |
| `experiment_variant` | String  | Variant the customer is in |
| `offering_id`        | String  | Offering ID of the variant |
| `enrolled_at_ms`     | Integer | Enrollment time (Unix ms)  |

## Tips

- **Trial detection**: `period_type == "TRIAL"`
- **Trial duration**: `expiration_at_ms - purchased_at_ms` (in ms)
- **Subscription active**: `expiration_at_ms > now`
- **Refund**: `CANCELLATION` + `cancel_reason == "CUSTOMER_SUPPORT"` + `price < 0`
- **Sandbox**: `environment == "SANDBOX"`
