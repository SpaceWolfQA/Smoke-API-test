import pytest
import requests
import time

from config.settings import set, get
from endpoints.base_endpoint import Endpoint


class CopyPlan(Endpoint):

    def copy_plan(self, url_bill, headers, payload, max_retries, wait_sec):
        plan_id = get('plan_id')
        for attempt in range(max_retries):
            try:
                self.response = requests.post(f'{url_bill}/v3/plans/{plan_id}/copy', headers=headers, json=payload)
                self.response.raise_for_status()
                copy_plan_id = self.response.json()['id']
                set('copy_plan_id', copy_plan_id)
                print('Response Status Code:', self.response.status_code)
                break

            except Exception as err:
                print(f'Attempt {attempt + 1 } failed:', err, self.response.json())
                if attempt < max_retries - 1:
                    print(f'Retrying in {wait_sec} seconds...')
                    time.sleep(wait_sec)
                else:
                    print('Max retries exceeded.')
                    raise

    def check_copy_plan(self, url_bill, headers):
        copy_plan_id = get('copy_plan_id')
        copy_plan_name = get('copy_plan_name_en')
        self.response = requests.get(f'{url_bill}/v3/plans/{copy_plan_id}', headers=headers)
        plan_name = self.response.json()['name_en']
        if plan_name != copy_plan_name:
            pytest.fail('Plan does not copied')
        print('Plan copied')
