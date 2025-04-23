import allure
import requests
import time

from config.settings import get
from endpoints.base_endpoint import Endpoint


class StartTrial(Endpoint):

    def start_trial(self, url_bill, headers, payload, max_retries, wait_sec):
        with allure.step('Get trial_id'):
            trial_id = get('trial_id')
        with allure.step('Start trial'):
            for attempt in range(max_retries):
                try:
                    self.response = requests.post(
                        f'{url_bill}/v3/trials/{trial_id}/start',
                        headers=headers,
                        json=payload
                    )
                    self.response.raise_for_status()
                    break

                except requests.HTTPError:
                    if self.response.status_code == 403:
                        break

                except Exception as err:
                    print(f'Attempt {attempt + 1} failed:', err, self.response.json())
                    if attempt < max_retries - 1:
                        time.sleep(wait_sec)
                    else:
                        raise

    def check_start(self, url_bill, headers, max_retries, wait_sec):
        with allure.step('Get test variable (trial_id)'):
            trial_id = get('trial_id')
        with allure.step('Check trial start'):
            for attempt in range(max_retries):
                try:
                    self.response = requests.get(f'{url_bill}/v3/trials/{trial_id}', headers=headers)
                    is_started = self.response.json()['started_at']
                    remainder_sec = self.response.json()['remainder_sec']
                    assert is_started is not None or remainder_sec is not None
                    break

                except Exception as err:
                    print(f'Attempt {attempt + 1} failed:', err, self.response.json())
                    if attempt < max_retries - 1:
                        time.sleep(wait_sec)
                    else:
                        raise
