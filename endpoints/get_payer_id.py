import requests
import time

from config.settings import get, set
from endpoints.base_endpoint import Endpoint


class GetPayerID(Endpoint):

    def get_payer_id(self, url_bill, headers, max_retries, wait_sec):
        client_id = get('client_id')
        for attempt in range(max_retries):
            try:
                self.response = requests.get(f'{url_bill}/v1/payers?client_id={client_id}&active=true', headers=headers)
                self.response.raise_for_status()
                payer_id = self.response.json()[0]['id']
                set('payer_id', payer_id)
                print('Response Status Code:', self.response.status_code)
                break

            except Exception as err:
                print(f'Attempt {attempt + 1} failed:', err, self.response.json())
                if attempt < max_retries - 1:
                    print(f'Retrying in {wait_sec} seconds...')
                    time.sleep(wait_sec)
                else:
                    print('Max retries exceeded')
