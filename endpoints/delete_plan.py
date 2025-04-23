import allure
import requests
import time

from config.settings import get
from endpoints.base_endpoint import Endpoint


class DeletePlan(Endpoint):

    def delete_plan(self, url_bill, headers, max_retries, wait_sec):
        with allure.step('Get plan_id'):
            plan_id = get('plan_id')
        with allure.step('Delete plan'):
            for attempt in range(max_retries):
                try:
                    self.response = requests.delete(f'{url_bill}/v3/plans/{plan_id}', headers=headers)
                    self.response.raise_for_status()
                    break

                except Exception as err:
                    print(f'Attempt {attempt + 1} failed:', err)
                    if attempt < max_retries - 1:
                        print(f'Retrying in {wait_sec} seconds...')
                        time.sleep(wait_sec)
                    else:
                        print('Max retries exceeded')
                        raise

    def check_deletion(self, url_bill, headers, max_retries, wait_sec):
        with allure.step('Get test variable (plan_id)'):
            plan_id = get('plan_id')
        with allure.step('Check plan deletion'):
            for attempt in range(max_retries):
                try:
                    self.response = requests.get(f'{url_bill}/v3/plans/{plan_id}', headers=headers)
                    assert self.response.status_code == 404
                    break

                except Exception as err:
                    print(f'Attempt {attempt + 1} failed:', err, self.response.json())
                    if attempt < max_retries - 1:
                        time.sleep(wait_sec)
                    else:
                        raise
