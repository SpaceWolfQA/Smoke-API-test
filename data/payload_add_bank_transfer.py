from config.settings import get


def add_bank_transfer_payload():
    return {"client_id": get('client_id')}
