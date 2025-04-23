import allure
import requests
import time

from config.settings import get
from endpoints.base_endpoint import Endpoint


class DeleteClient(Endpoint):

    def delete_client(self, url_iam, headers, payload, max_retries, wait_sec):
        with allure.step('Get client_id'):
            client_id = get('client_id')
        with allure.step('Delete client'):
            for attempt in range(max_retries):
                try:
                    self.response = requests.patch(
                        f'{url_iam}/clients/{client_id}/delete_request',
                        headers=headers,
                        json=payload
                    )
                    self.response.raise_for_status()
                    break

                except Exception as err:
                    print(f'Attempt {attempt + 1} failed', err, self.response.json())
                    if attempt < max_retries - 1:
                        time.sleep(wait_sec)
                    else:
                        raise

    def check_deletion(self, url_iam, headers, max_retries, wait_sec):
        with allure.step('Get test variable (client_id)'):
            client_id = get('client_id')
        with allure.step('Check client deletion'):
            for attempt in range(max_retries):
                try:
                    self.response = requests.get(f'{url_iam}/clients/{client_id}', headers=headers)
                    get_email = self.response.json()['email']
                    email = get('email')
                    assert get_email != email
                    break

                except Exception as err:
                    print(f'Attempt {attempt + 1} failed', err, self.response.json())
                    if attempt < max_retries - 1:
                        time.sleep(wait_sec)
                    else:
                        raise
