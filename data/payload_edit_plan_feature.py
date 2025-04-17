from config.settings import get


def edit_plan_feature_payload():
    plan_id = get('plan_id')
    feature_id = get('feature_id')
    return {
        "default": False,
        "plan_id": plan_id,
        "plan_item": {
            "activity_period": "month",
            "activity_period_length": "1",
            "calc_rule_id": 1,
            "default_value": "1",
            "feature_id": feature_id,
            "feature_sap_id": feature_id,
            "unit_size": "2",
            "unit_id": 34,
            "recurring_type": "MRC",
            "price": {
                "currency_id": 3,
                "money_value": "3"
            }
        }
    }
