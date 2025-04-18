import pytest
import requests
import time

from config.settings import set, get
from endpoints.base_endpoint import Endpoint


class CreateContract(Endpoint):

    def create_contract(self, url_bill, headers, payload, max_retries, wait_sec):
        for attempt in range(max_retries):
            try:
                self.response = requests.post(f'{url_bill}/v1/contracts', headers=headers, json=payload)
                self.response.raise_for_status()
                contract_id = self.response.json()['id']
                set('contract_id', contract_id)
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

    def check_creation(self, url_bill, headers, max_retries, wait_sec):
        payer_id = get('payer_id')
        contract_id = get('contract_id')
        for attempt in range(max_retries):
            try:
                self.response = requests.get(f'{url_bill}/v1/contracts/{contract_id}', headers=headers)
                get_payer_id = self.response.json()['payer_id']
                if payer_id != get_payer_id:
                    pytest.fail('Contract does not created')
                print('Contract created')
                break

            except Exception as err:
                print(f'Attempt {attempt + 1} failed:', err, self.response.json())
                if attempt < max_retries - 1:
                    print(f'Retrying in {wait_sec} seconds...')
                    time.sleep(wait_sec)
                else:
                    print('Max retries exceeded.')
                    raise
