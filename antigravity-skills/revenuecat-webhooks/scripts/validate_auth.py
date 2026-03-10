python
#!/usr/bin/env python3
import sys

def validate_webhook_auth(headers, expected_token):
    """
    Validates the authorization header from a RevenueCat webhook.
    Usage: validate_auth.py "Bearer my_token" "Bearer my_token"
    """
    if len(sys.argv) < 3:
        print("Usage: validate_auth.py <incoming_header> <expected_token>")
        sys.exit(1)

    incoming_header = sys.argv[1]
    expected_token = sys.argv[2]

    if not incoming_header:
        print("Status: 401 Unauthorized - Missing Authorization header")
        sys.exit(1)

    if incoming_header != expected_token:
        print("Status: 401 Unauthorized - Invalid Authorization token")
        sys.exit(1)

    print("Status: 200 OK - Valid token")
    sys.exit(0)

if __name__ == "__main__":
    validate_webhook_auth(sys.argv, sys.argv)