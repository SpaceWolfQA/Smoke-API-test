import pytest
import requests
import time

from config.settings import get
from endpoints.base_endpoint import Endpoint


class UpdateTrial(Endpoint):

    def update_trial(self, url_bill, headers, payload, max_retries, wait_sec):
        trial_id = get('trial_id')
        for attempt in range(max_retries):
            try:
                self.response = requests.put(f'{url_bill}/v3/trials/{trial_id}', headers=headers, json=payload)
                self.response.raise_for_status()
                print('Response Status Code:', self.response.status_code)
                break

            except Exception as err:
                print(f'Attempt {attempt + 1} failed:', err, self.response.json())
                if attempt < max_retries - 1:
                    print(f'Retrying in {wait_sec} seconds...')
                    time.sleep(wait_sec)
                else:
                    print('Max retries exceeded')

    def check_update_trial(self, url_bill, headers):
        trial_id = get('trial_id')
        update_trial_contract_id = get('contract_id')
        self.response = requests.get(f'{url_bill}/v3/trials/{trial_id}', headers=headers)
        contract_id = self.response.json()['contract_id']
        days_limit = self.response.json()['days_limit']
        if update_trial_contract_id != contract_id and days_limit != 14:
            pytest.fail('Trial does not updated')
        print('Trial updated')
