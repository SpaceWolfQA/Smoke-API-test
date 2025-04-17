from config.settings import get


def update_trial_payload():
    contract_id = get('contract_id')
    trial_id = get('trial_id')
    return {
        "contract_id": contract_id,
        "days_limit": "14",
        "id": trial_id
    }
