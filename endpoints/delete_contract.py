import time

import allure
import requests

from endpoints.base_endpoint import Endpoint
from config.settings import get


class DeleteContract(Endpoint):

    def delete_contract(self, url_bill, headers, max_retries, wait_sec):
        with allure.step('Get contract_id'):
            contract_id = get('contract_id')
        with allure.step('Delete contract'):
            for attempt in range(max_retries):
                try:
                    self.response = requests.delete(f'{url_bill}/v1/contracts/{contract_id}', headers=headers)
                    self.response.raise_for_status()
                    break

                except Exception as err:
                    print(f'Attempt {attempt + 1} failed.', err, self.response.json())
                    if attempt < max_retries - 1:
                        time.sleep(wait_sec)
                    else:
                        raise

    def check_deletion(self, url_bill, headers, max_retries, wait_sec):
        with allure.step('Get test variable (contract_id)'):
            contract_id = get('contract_id')
        with allure.step('Check contract deletion'):
            for attempt in range(max_retries):
                try:
                    self.response = requests.get(f'{url_bill}/v1/contracts/{contract_id}', headers=headers)
                    assert self.response.status_code == 404
                    break

                except Exception as err:
                    print(f'Attempt {attempt + 1} failed.', err, self.response.json())
                    if attempt < max_retries - 1:
                        time.sleep(wait_sec)
                    else:
                        raise
