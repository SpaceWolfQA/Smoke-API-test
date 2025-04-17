from config.settings import get
from data.date_and_time import *


def create_expense_payload():
    client_id = get('client_id')
    contract_id = get('contract_id')
    return {
        "client_id": client_id,
        "contract_id": contract_id,
        "plan_id": 2479,
        "plan_item_id": 387487,
        "for_date": get_today_date(),
        "period_date": get_today_date(),
        "usage": "10000",
        "money_value": "12000"
        }
