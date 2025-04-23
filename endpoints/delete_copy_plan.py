import allure
import requests
import time

from config.settings import get
from endpoints.base_endpoint import Endpoint


class DeleteCopyPlan(Endpoint):

    def delete_copy_plan(self, url_bill, headers, max_retries, wait_sec):
        with allure.step('Get copy_plan_id'):
            copy_plan_id = get('copy_plan_id')
        with allure.step('Delete copy plan'):
            for attempt in range(max_retries):
                try:
                    self.response = requests.delete(f'{url_bill}/v3/plans/{copy_plan_id}', headers=headers)
                    self.response.raise_for_status()
                    break

                except Exception as err:
                    print(f'Attempt {attempt + 1} failed:', err)
                    if attempt < max_retries - 1:
                        time.sleep(wait_sec)
                    else:
                        raise

    def check_deletion(self, url_bill, headers, max_retries, wait_sec):
        with allure.step('Get test variable (copy_plan_id)'):
            copy_plan_id = get('copy_plan_id')
        with allure.step('Check copy plan deletion'):
            for attempt in range(max_retries):
                try:
                    self.response = requests.get(f'{url_bill}/v3/plans/{copy_plan_id}', headers=headers)
                    assert self.response.status_code == 404
                    break

                except Exception as err:
                    print(f'Attempt {attempt + 1} failed:', err)
                    if attempt < max_retries - 1:
                        time.sleep(wait_sec)
                    else:
                        raise
