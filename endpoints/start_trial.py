import pytest
import requests
import time

from config.settings import get
from endpoints.base_endpoint import Endpoint


class StartTrial(Endpoint):

    def start_trial(self, url_bill, headers, payload, max_retries, wait_sec):
        trial_id = get('trial_id')
        for attempt in range(max_retries):
            try:
                self.response = requests.post(f'{url_bill}/v3/trials/{trial_id}/start', headers=headers, json=payload)
                self.response.raise_for_status()
                print('Response Status Code:', self.response.status_code)
                break

            except requests.HTTPError as err:
                if self.response.status_code == 403:
                    print('Sync error, try later')
                print(f'Attempt {attempt} failed, Error:', err)

            except Exception as err:
                print(f'Attempt {attempt + 1} failed:', err, self.response.json())
                if attempt < max_retries - 1:
                    print(f'Retrying in {wait_sec} seconds...')
                    time.sleep(wait_sec)
                else:
                    print('Max retries exceeded')
                    raise

    def check_start(self, url_bill, headers, max_retries, wait_sec):
        trial_id = get('trial_id')
        for attempt in range(max_retries):
            try:
                self.response = requests.get(f'{url_bill}/v3/trials/{trial_id}', headers=headers)
                is_started = self.response.json()['started_at']
                remainder_sec = self.response.json()['remainder_sec']
                if is_started is None or remainder_sec is None:
                    pytest.fail('Trial does not started')
                print('Trial started')
                break

            except Exception as err:
                print(f'Attempt {attempt + 1} failed:', err, self.response.json())
                if attempt < max_retries - 1:
                    print(f'Retrying in {wait_sec} seconds...')
                    time.sleep(wait_sec)
                else:
                    print('Max retries exceeded')
                    raise
