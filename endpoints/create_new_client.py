import pytest
import requests
import time

from config.settings import set, get
from endpoints.base_endpoint import Endpoint


class CreateClient(Endpoint):
    def new_client(self, url_iam, headers, payload, max_retries, wait_sec):
        for attempt in range(max_retries):
            try:
                self.response = requests.post(f'{url_iam}/users', headers=headers, json=payload)
                self.response.raise_for_status()
                client_id = self.response.json()['client']
                set('client_id', client_id)
                print('Response Status Code:', self.response.status_code)
                break

            except Exception as err:
                print(f'Attempt {attempt + 1} failed:', err, self.response.json())
                if attempt < max_retries - 1:
                    print(f'Retrying in {wait_sec} seconds...')
                    time.sleep(wait_sec)
                else:
                    print('Max retries exceeded.')
                    raise

    def check_creation(self, url_iam, headers, max_retries, wait_sec):
        client_id = get('client_id')
        email = get('email')
        company = get('company')
        for attempt in range(max_retries):
            try:
                self.response = requests.get(f'{url_iam}/clients/{client_id}', headers=headers)
                client_email = self.response.json()['email']
                client_company = self.response.json()['companyName']
                if email != client_email and company != client_company:
                    pytest.fail('Error creating client')
                print('New Client created')
                break

            except Exception as err:
                print(f'Attempt {attempt + 1} failed:', err, self.response.json())
                if attempt < max_retries - 1:
                    print(f'Retrying in {wait_sec} seconds...')
                    time.sleep(wait_sec)
                else:
                    print('Max retries exceeded.')
                    raise
