import pytest
import requests
import time

from config.settings import get
from endpoints.base_endpoint import Endpoint


class EditPlan(Endpoint):

    def edit_plan(self, url_bill, headers, payload, max_retries, wait_sec):
        plan_id = get('plan_id')
        for attempt in range(max_retries):
            try:
                self.response = requests.put(f'{url_bill}/v3/plans/{plan_id}', headers=headers, json=payload)
                self.response.raise_for_status()
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

    def check_edit(self, url_bill, headers):
        plan_id = get('plan_id')
        edited_plan_name = get('edit_plan_name_en')
        self.response = requests.get(f'{url_bill}/v3/plans/{plan_id}', headers=headers)
        plan_name = self.response.json()['name_en']
        if edited_plan_name != plan_name:
            pytest.fail('Plan does not edit')
        print('Plan edited')
