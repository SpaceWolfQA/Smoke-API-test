from data.client_data import *


new_client_payload = {
    "company": generate_company(),
    "email": generate_email(),
    "password": generate_password(),
    "services": [
        {
            "product_name": "CDN",
            "available": None
        },
        {
            "product_name": "STREAMING",
            "available": None
        },
        {
            "product_name": "CLOUD",
            "available": None
        },
        {
            "product_name": "STORAGE",
            "available": None
        },
        {
            "product_name": "DDOS",
            "available": None
        },
        {
            "product_name": "HOSTING",
            "available": None
        },
        {
            "product_name": "INFRASTRUCTURE_PROTECTION",
            "available": None
        },
        {
            "product_name": "DNS",
            "available": None
        },
        {
            "product_name": "CONNECT",
            "available": None
        },
        {
            "product_name": "STRESS_TESTING",
            "available": None
        }
    ],
    "is_test": True,
    "reseller": 75755
}
