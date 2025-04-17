import pytest
import requests
import time

from config.settings import set, get
from endpoints.base_endpoint import Endpoint


class CreatePlan(Endpoint):

    def create_plan(self, url_bill, headers, payload, max_retries, wait_sec):
        for attempt in range(max_retries):
            try:
                self.response = requests.post(f'{url_bill}/v3/plans', headers=headers, json=payload)
                self.response.raise_for_status()
                plan_id = self.response.json()['id']
                set('plan_id', plan_id)
                print('Plan ID:', plan_id)
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

    def check_creation(self, url_bill, headers):
        plan_id = get('plan_id')
        created_plan_name = get('create_plan_name_en')
        self.response = requests.get(f'{url_bill}/v3/plans/{plan_id}', headers=headers)
        plan_name = self.response.json()['name_en']
        if plan_name != created_plan_name:
            pytest.fail('Plan does not created')
        print('Plan created')
