import uuid

from config.settings import set, get


def edit_feature_payload():
    edit_feature_name_en = str(uuid.uuid4())
    set('edit_feature_name_en', edit_feature_name_en)
    metric_id = get('metric_id')
    return {
        "billing_service_id": None,
        "name_en": edit_feature_name_en,
        "name_ru": None,
        "product_id": 1,
        "sap_id": None,
        "metric_id": metric_id,
        "region_id": None,
        "statistic_unit_id": 34,
        "rounding_rule": None,
        "metrics": [
            metric_id
        ],
        "regions": []
    }
