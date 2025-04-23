import allure
import requests
import time

from config.settings import get
from endpoints.base_endpoint import Endpoint


class EditPlan(Endpoint):

    def edit_plan(self, url_bill, headers, payload, max_retries, wait_sec):
        with allure.step('Get plan_id'):
            plan_id = get('plan_id')
        with allure.step('Edit plan'):
            for attempt in range(max_retries):
                try:
                    self.response = requests.put(f'{url_bill}/v3/plans/{plan_id}', headers=headers, json=payload)
                    self.response.raise_for_status()
                    break

                except Exception as err:
                    print(f'Attempt {attempt + 1 } failed:', err, self.response.json())
                    if attempt < max_retries - 1:
                        time.sleep(wait_sec)
                    else:
                        raise

    def check_change(self, url_bill, headers, max_retries, wait_sec):
        with allure.step('Get test variables (plan_id, edit_plan_name)'):
            plan_id = get('plan_id')
            edited_plan_name = get('edit_plan_name_en')
        with allure.step('Check plan change'):
            for attempt in range(max_retries):
                try:
                    self.response = requests.get(f'{url_bill}/v3/plans/{plan_id}', headers=headers)
                    plan_name = self.response.json()['name_en']
                    assert edited_plan_name == plan_name
                    break

                except Exception as err:
                    print(f'Attempt {attempt + 1 } failed:', err, self.response.json())
                    if attempt < max_retries - 1:
                        time.sleep(wait_sec)
                    else:
                        raise
