from config.settings import get
from data.date_and_time import *


def create_contract_payload():
    return {
        "provider_id": 47632,
        "payer_id": get("payer_id"),
        "valid_from": str(get_today_date()),
        "valid_to": str(get_tomorrow_date()),
        "contract_type_id": "Z00",
        "synced": False
    }