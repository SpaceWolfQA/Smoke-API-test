from config.settings import get
from data.date_and_time import *


def create_addendum_payload():
    client_id = get('client_id')
    contract_id = get('contract_id')
    return {
        "client_id": client_id,
        "contract_id": contract_id,
        "plan_id": 2479, #исправить этот момент на создаваемый план
        "active_from": get_yesterday_date(),
        "active_to": get_tomorrow_date()
    }