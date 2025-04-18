import pytest
import requests
import time

from config.settings import get
from endpoints.base_endpoint import Endpoint


class DeleteCopyPlan(Endpoint):

    def delete_copy_plan(self, url_bill, headers, max_retries, wait_sec):
        copy_plan_id = get('copy_plan_id')
        for attempt in range(max_retries):
            try:
                self.response = requests.delete(f'{url_bill}/v3/plans/{copy_plan_id}', headers=headers)
                self.response.raise_for_status()
                print('Response Status Code:', self.response.status_code)
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
        for attempt in range(max_retries):
            try:
                copy_plan_id = get('copy_plan_id')
                self.response = requests.get(f'{url_bill}/v3/plans/{copy_plan_id}', headers=headers)
                if self.response.status_code != 404:
                    pytest.fail('Copied plan does not deleted')
                print('Copied plan deleted')
                break

            except Exception as err:
                print(f'Attempt {attempt + 1} failed:', err)
                if attempt < max_retries - 1:
                    print(f'Retrying in {wait_sec} seconds...')
                    time.sleep(wait_sec)
                else:
                    print('Max retries exceeded')
                    raise
