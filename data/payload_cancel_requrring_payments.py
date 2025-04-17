from config.settings import get


def cancel_recurring_payments_payload():
    return {
        "product_management": "BILLING",
        "provider_id": 9110,
        "currency_id": 3,
        "tax": {
            "value": 17,
            "type": "excluded"
        },
        "recurring_payments": False,
        "checking_balance": False,
        "postpaid": False,
        "client_id": get('client_id'),
        "country_tax": 20
    }