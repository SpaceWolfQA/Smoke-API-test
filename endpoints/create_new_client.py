import allure
import requests
import time

from config.settings import set, get
from endpoints.base_endpoint import Endpoint


class CreateClient(Endpoint):
    def new_client(self, url_iam, headers, payload, max_retries, wait_sec):
        with allure.step('Create new client'):
            for attempt in range(max_retries):
                try:
                    self.response = requests.post(f'{url_iam}/users', headers=headers, json=payload)
                    self.response.raise_for_status()
                    client_id = self.response.json()['client']
                    set('client_id', client_id)
                    break

                except Exception as err:
                    print(f'Attempt {attempt + 1} failed:', err, self.response.json())
                    if attempt < max_retries - 1:
                        time.sleep(wait_sec)
                    else:
                        raise

    def check_creation(self, url_iam, headers, max_retries, wait_sec):
        with allure.step('Get test variables (client_id, email, company)'):
            client_id = get('client_id')
            email = get('email')
            company = get('company')
        with allure.step('Check client creation'):
            for attempt in range(max_retries):
                try:
                    self.response = requests.get(f'{url_iam}/clients/{client_id}', headers=headers)
                    client_email = self.response.json()['email']
                    client_company = self.response.json()['companyName']
                    assert email == client_email and company == client_company
                    break

                except Exception as err:
                    print(f'Attempt {attempt + 1} failed:', err, self.response.json())
                    if attempt < max_retries - 1:
                        time.sleep(wait_sec)
                    else:
                        raise
