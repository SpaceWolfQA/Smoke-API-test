import uuid

from config.settings import set


def create_plan_payload():
    create_plan_name_en = str(uuid.uuid4())
    set('create_plan_name_en', create_plan_name_en)
    return {
        "name_en": create_plan_name_en,
        "product_id": 1,
        "currency_id": 3,
        "tax_type": "excluded"
    }