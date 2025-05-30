import allure
import requests
import time

from config.settings import get, set
from endpoints.base_endpoint import Endpoint


class GetPayerID(Endpoint):

    def get_payer_id(self, url_bill, headers, max_retries, wait_sec):
        with allure.step('Get client_id'):
            client_id = get('client_id')
        with allure.step('Get payer_id'):
            for attempt in range(max_retries):
                try:
                    self.response = requests.get(f'{url_bill}/v1/payers?client_id={client_id}&active=true', headers=headers)
                    self.response.raise_for_status()
                    payer_id = self.response.json()[0]['id']
                    set('payer_id', payer_id)
                    break

                except Exception as err:
                    print(f'Attempt {attempt + 1} failed:', err, self.response.json())
                    if attempt < max_retries - 1:
                        time.sleep(wait_sec)
                    else:
                        raise
