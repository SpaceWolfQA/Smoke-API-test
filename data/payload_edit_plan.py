import uuid

from config.settings import set


def edit_plan_payload():
    edit_plan_name_en = str(uuid.uuid4())
    set('edit_plan_name_en', edit_plan_name_en)
    return {
        "name_en": edit_plan_name_en,
        "product_id": 1,
        "currency_id": 3,
        "tax_type": "excluded"
    }
