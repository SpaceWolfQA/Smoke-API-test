from config.settings import get
from data.date_and_time import *


def create_invoice_payload():
    client_id = get('client_id')
    return {
        "client_id": client_id,
        "currency_id": 3,
        "invoice_date": get_today_date(),
        "date_from": get_start_month(),
        "date_to": get_tomorrow_date()
    }
