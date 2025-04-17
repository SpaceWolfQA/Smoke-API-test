import pytest
import requests
import time

from config.settings import get
from endpoints.base_endpoint import Endpoint


class EditPlanFeature(Endpoint):

    def edit_plan_feature(self, url_bill, headers, payload, max_retries, wait_sec):
        plan_id = get('plan_id')
        plan_feature_id = get('plan_feature_id')
        for attempt in range(max_retries):
            try:
                self.response = requests.put(
                    f'{url_bill}/v3/plans/{plan_id}/content/{plan_feature_id}',
                    headers=headers,
                    json=payload
                )
                self.response.raise_for_status()
                print('Response Status Code:', self.response.status_code)
                break

            except Exception as err:
                print(f'Attempt {attempt + 1} failed:', err, self.response.json())
                if attempt < max_retries - 1:
                    print(f'Retrying in {wait_sec} seconds...')
                    time.sleep(wait_sec)
                else:
                    print('Max retries exceeded.')
                    raise

    def check_edit(self, url_bill, headers):
        plan_id = get('plan_id')
        plan_feature_id = get('plan_feature_id')
        add_feature_name = get('edit_feature_name_en')
        self.response = requests.get(f'{url_bill}/v3/plans/{plan_id}/content/{plan_feature_id}', headers=headers)
        feature_name = self.response.json()['plan_item']['feature_name']
        unit_size = self.response.json()['plan_item']['unit_size']
        default_value = self.response.json()['plan_item']['default_value']
        money_value = self.response.json()['plan_item']['price']['money_value']
        if (feature_name != add_feature_name
                and float(unit_size) != 2
                and float(default_value) != 1
                and float(money_value) != 3):
            pytest.fail('Feature does not added to plan')
        print("Feature added to plan")
