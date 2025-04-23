import allure
import requests
import time

from config.settings import set, get
from endpoints.base_endpoint import Endpoint


class CreatePlan(Endpoint):

    def create_plan(self, url_bill, headers, payload, max_retries, wait_sec):
        with allure.step('Create plan'):
            for attempt in range(max_retries):
                try:
                    self.response = requests.post(f'{url_bill}/v3/plans', headers=headers, json=payload)
                    self.response.raise_for_status()
                    plan_id = self.response.json()['id']
                    set('plan_id', plan_id)
                    break

                except Exception as err:
                    print(f'Attempt {attempt + 1} failed:', err, self.response.json())
                    if attempt < max_retries - 1:
                        time.sleep(wait_sec)
                    else:
                        raise

    def check_creation(self, url_bill, headers, max_retries, wait_sec):
        with allure.step('Get test variables (plan_id, created_plan_name)'):
            plan_id = get('plan_id')
            created_plan_name = get('create_plan_name_en')
        with allure.step('Check plan creation'):
            for attempt in range(max_retries):
                try:
                    self.response = requests.get(f'{url_bill}/v3/plans/{plan_id}', headers=headers)
                    plan_name = self.response.json()['name_en']
                    assert plan_name == created_plan_name
                    break

                except Exception as err:
                    print(f'Attempt {attempt + 1} failed:', err, self.response.json())
                    if attempt < max_retries - 1:
                        time.sleep(wait_sec)
                    else:
                        raise
