import allure
import requests
import time

from config.settings import set, get
from endpoints.base_endpoint import Endpoint


class CopyPlan(Endpoint):

    def copy_plan(self, url_bill, headers, payload, max_retries, wait_sec):
        with allure.step('Get plan_id'):
            plan_id = get('plan_id')
        with allure.step('Copy plan'):
            for attempt in range(max_retries):
                try:
                    self.response = requests.post(f'{url_bill}/v3/plans/{plan_id}/copy', headers=headers, json=payload)
                    self.response.raise_for_status()
                    copy_plan_id = self.response.json()['id']
                    set('copy_plan_id', copy_plan_id)
                    break

                except Exception as err:
                    print(f'Attempt {attempt + 1 } failed:', err, self.response.json())
                    if attempt < max_retries - 1:
                        time.sleep(wait_sec)
                    else:
                        raise

    def check_copy_plan(self, url_bill, headers, max_retries, wait_sec):
        with allure.step('Get test variables (copy_plan_id, copy_plan_name_en)'):
            copy_plan_id = get('copy_plan_id')
            copy_plan_name = get('copy_plan_name_en')
        with allure.step('Check copy plan'):
            for attempt in range(max_retries):
                try:
                    self.response = requests.get(f'{url_bill}/v3/plans/{copy_plan_id}', headers=headers)
                    plan_name = self.response.json()['name_en']
                    assert plan_name == copy_plan_name
                    break

                except Exception as err:
                    print(f'Attempt {attempt + 1 } failed:', err, self.response.json())
                    if attempt < max_retries - 1:
                        time.sleep(wait_sec)
                    else:
                        raise
