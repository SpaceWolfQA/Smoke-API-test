import time

import pytest
import requests
from endpoints.base_endpoint import Endpoint
from config.settings import get


class DeleteContract(Endpoint):

    def delete_contract(self, url_bill, headers, max_retries, wait_sec):
        contract_id = get('contract_id')
        for attempt in range(max_retries):
            try:
                self.response = requests.delete(f'{url_bill}/v1/contracts/{contract_id}', headers=headers)
                self.response.raise_for_status()
                print('Response Status Code:', self.response.status_code)
                break

            except Exception as err:
                print(f'Attempt {attempt + 1} failed.', err, self.response.json())
                if attempt < max_retries - 1:
                    print(f'Retrying in {wait_sec} seconds...')
                    time.sleep(wait_sec)
                else:
                    print('Max retries exceeded.')
                    raise

    def check_deletion(self, url_bill, headers):
        contract_id = get('contract_id')
        self.response = requests.get(f'{url_bill}/v1/contracts/{contract_id}', headers=headers)
        if self.response.status_code != 404:
            pytest.fail('Contract does not deleted')
        print('Contract deleted')
