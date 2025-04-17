import requests
import time

from config.settings import get, set
from endpoints.base_endpoint import Endpoint


class GetTrialID(Endpoint):

    def get_trial_id(self, url_bill, headers, max_retries, wait_sec):
        client_id = get('client_id')
        for attempt in range(max_retries):
            try:
                self.response = requests.get(
                    f'{url_bill}/v3/trials?client_id={client_id}&product_id=2&limit=10',
                    headers=headers
                )
                self.response.raise_for_status()
                trial_id = self.response.json()['results'][0]['id']
                print(trial_id)
                set('trial_id', trial_id)
                print('Response Status Code:', self.response.status_code)
                break

            except Exception as err:
                print(f'Attempt {attempt + 1} failed:', err, self.response.json())
                if attempt < max_retries - 1:
                    print(f'Retrying in {wait_sec} seconds...')
                    time.sleep(wait_sec)
                else:
                    print('Max retries exceeded')
