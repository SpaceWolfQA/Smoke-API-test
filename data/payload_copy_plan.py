import uuid

from config.settings import set


def copy_plan_payload():
    copy_plan_name_en = str(uuid.uuid4())
    set('copy_plan_name_en', copy_plan_name_en)
    return {
        "name_en": copy_plan_name_en,
        "product_id": 1,
        "currency_id": 3,
        "tax_type": "excluded"
    }
