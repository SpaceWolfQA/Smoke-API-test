import allure
import requests
import time

from config.settings import get
from endpoints.base_endpoint import Endpoint


class EditPlanFeature(Endpoint):

    def edit_plan_feature(self, url_bill, headers, payload, max_retries, wait_sec):
        with allure.step('Get plan_id and plan_feature_id'):
            plan_id = get('plan_id')
            plan_feature_id = get('plan_feature_id')
        with allure.step('Edit plan feature'):
            for attempt in range(max_retries):
                try:
                    self.response = requests.put(
                        f'{url_bill}/v3/plans/{plan_id}/content/{plan_feature_id}',
                        headers=headers,
                        json=payload
                    )
                    self.response.raise_for_status()
                    break

                except Exception as err:
                    print(f'Attempt {attempt + 1} failed:', err, self.response.json())
                    if attempt < max_retries - 1:
                        time.sleep(wait_sec)
                    else:
                        raise

    def check_change(self, url_bill, headers, max_retries, wait_sec):
        with allure.step('Get test variables (plan_id, plan_feature_id, add_feature_name)'):
            plan_id = get('plan_id')
            plan_feature_id = get('plan_feature_id')
            add_feature_name = get('edit_feature_name_en')
        with allure.step('Check plan feature changed'):
            for attempt in range(max_retries):
                try:
                    self.response = requests.get(
                        f'{url_bill}/v3/plans/{plan_id}/content/{plan_feature_id}',
                        headers=headers
                    )
                    feature_name = self.response.json()['plan_item']['feature_name']
                    unit_size = self.response.json()['plan_item']['unit_size']
                    default_value = self.response.json()['plan_item']['default_value']
                    money_value = self.response.json()['plan_item']['price']['money_value']
                    assert (feature_name == add_feature_name
                            and float(unit_size) == 2
                            and float(default_value) == 1
                            and float(money_value) == 3)
                    break

                except Exception as err:
                    print(f'Attempt {attempt + 1} failed:', err, self.response.json())
                    if attempt < max_retries - 1:
                        time.sleep(wait_sec)
                    else:
                        raise
