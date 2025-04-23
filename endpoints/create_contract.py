import allure
import requests
import time

from config.settings import set, get
from endpoints.base_endpoint import Endpoint


class CreateContract(Endpoint):

    def create_contract(self, url_bill, headers, payload, max_retries, wait_sec):
        with allure.step('Create contract'):
            for attempt in range(max_retries):
                try:
                    self.response = requests.post(f'{url_bill}/v1/contracts', headers=headers, json=payload)
                    self.response.raise_for_status()
                    contract_id = self.response.json()['id']
                    set('contract_id', contract_id)
                    break

                except Exception as err:
                    print(f'Attempt {attempt + 1} failed:', err, self.response.json())
                    if attempt < max_retries - 1:
                        time.sleep(wait_sec)
                    else:
                        raise

    def check_creation(self, url_bill, headers, max_retries, wait_sec):
        with allure.step('Get test variables (payer_id, contract_id)'):
            payer_id = get('payer_id')
            contract_id = get('contract_id')
        with allure.step('Check contract creation'):
            for attempt in range(max_retries):
                try:
                    self.response = requests.get(f'{url_bill}/v1/contracts/{contract_id}', headers=headers)
                    get_payer_id = self.response.json()['payer_id']
                    assert payer_id == get_payer_id
                    break

                except Exception as err:
                    print(f'Attempt {attempt + 1} failed:', err, self.response.json())
                    if attempt < max_retries - 1:
                        time.sleep(wait_sec)
                    else:
                        raise
