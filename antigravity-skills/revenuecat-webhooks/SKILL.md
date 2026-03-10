---
name: revenuecat-webhooks
description: Provides guidelines, JSON payload schemas, and event types for implementing and validating RevenueCat Webhooks for auto-renewing subscriptions and in-app purchases.
---

# RevenueCat Webhooks Skill

You are an expert at integrating RevenueCat Webhooks into backend systems. RevenueCat sends server-to-server HTTP POST requests to a specified URL when events occur for a user's subscription or in-app purchase.

## Operating Instructions

1. **Setup & Best Practices:** - If the user needs help configuring the webhook, authenticating the request, or understanding delivery/retry logic, read `cat references/setup-and-delivery.md`.
   - **Crucial Rule:** Always advise the user to return a `200 OK` status code immediately upon receiving the webhook, *before* processing the payload. RevenueCat will retry up to 5 times if a 200 series status code is not received.

2. **Parsing Payloads & Event Types:**
   - If the user asks about specific JSON fields, how to differentiate events, or needs a data model/DTO generated, read `cat references/event-types-and-fields.md`.
   - RevenueCat sends a single JSON object containing an `event` object. The `type` field dictates the action (e.g., `INITIAL_PURCHASE`, `RENEWAL`, `CANCELLATION`).

3. **Security/Validation:**
   - RevenueCat uses an Authorization header (Bearer token) for security.
   - You can execute `scripts/validate_auth.py` to test auth header validation logic if needed.

## Common Agent Workflows
- **Generate a Webhook Controller:** Read both reference files, then generate an endpoint (Node.js, C#, Python, etc.) that checks the Authorization header, returns 200 OK immediately, and queues the payload for processing.
- **Data Modeling:** Read `references/event-types-and-fields.md` and generate TypeScript interfaces, C# records, or Python Pydantic models for the webhook payloads.