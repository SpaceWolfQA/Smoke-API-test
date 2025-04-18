import pytest
import requests
import time
from endpoints.base_endpoint import Endpoint
from config.settings import get


class UpdateClient(Endpoint):

    def update_signup(self, url_iam, headers, payload, max_retries, wait_sec):
        client_id = get('client_id')
        for attempt in range(max_retries):
            try:
                self.response = requests.put(f'{url_iam}/clients/{client_id}', headers=headers, json=payload)
                self.response.raise_for_status()
                print('Response Status Code:', self.response.status_code)
                break
            except Exception as err:
                print(f'Attempt {attempt + 1} failed', err, self.response.json())
                if attempt < max_retries - 1:
                    print(f'Retrying in {wait_sec} seconds...')
                    time.sleep(wait_sec)
                else:
                    print('Max retries exceeded.')
                    raise

    def cancel_recurring_payments(self, url_bill, headers, payload, max_retries, wait_sec):
        client_id = get('client_id')
        for attempt in range(max_retries):
            try:
                self.response = requests.put(
                    f'{url_bill}/v1/clients/{client_id}/options',
                    headers=headers,
                    json=payload
                )
                self.response.raise_for_status()
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

    def delete_yoomoney(self, url_bill, headers, max_retries, wait_sec):
        client_id = get('client_id')
        for attempt in range(max_retries):
            try:
                self.response = requests.delete(
                    f'{url_bill}/v1/payment_methods/21/allowed/{client_id}',
                    headers=headers
                )
                self.response.raise_for_status()
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

    def add_bank_transfer(self, url_bill, headers, payload, max_retries, wait_sec):
        for attempt in range(max_retries):
            try:
                self.response = requests.post(
                    f'{url_bill}/v1/payment_methods/16/allowed',
                    headers=headers,
                    json=payload
                )
                self.response.raise_for_status()
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

    def check_signup(self, url_iam, headers, max_retries, wait_sec):
        client_id = get('client_id')
        for attempt in range(max_retries):
            try:
                self.response = requests.get(f'{url_iam}/clients/{client_id}', headers=headers)
                current_signup = self.response.json()['signup_process']
                if current_signup is not None:
                    pytest.fail('Sign Up does not updated')
                print('Sign Up updated')
                break

            except Exception as err:
                print(f'Attempt {attempt + 1} failed:', err, self.response.json())
                if attempt < max_retries - 1:
                    print(f'Retrying in {wait_sec} seconds...')
                    time.sleep(wait_sec)
                else:
                    print('Max retries exceeded.')
                    raise

    def check_recurring_payments(self, url_bill, headers, max_retries, wait_sec):
        client_id = get('client_id')
        for attempt in range(max_retries):
            try:
                self.response = requests.get(f'{url_bill}/v1/clients/{client_id}/options', headers=headers)
                current_recurring_payments = self.response.json()['recurring_payments']
                if current_recurring_payments is True:
                    pytest.fail('Recurring Payments does not cancel')
                print(f'Recurring Payments canceled')
                break

            except Exception as err:
                print(f'Attempt {attempt + 1} failed:', err, self.response.json())
                if attempt < max_retries - 1:
                    print(f'Retrying in {wait_sec} seconds...')
                    time.sleep(wait_sec)
                else:
                    print('Max retries exceeded.')
                    raise

    def check_payments_methods(self, url_bill, headers, max_retries, wait_sec):
        client_id = get('client_id')
        for attempt in range(max_retries):
            try:
                self.response = requests.get(f'{url_bill}/v1/payment_methods?client_id={client_id}', headers=headers)
                payments_methods = self.response.json()
                if len(payments_methods) != 1 and payments_methods[0]['name'] != 'bank':
                    pytest.fail('Error Changing Payments Methods')
                print('Payment Methods updated')
                break

            except Exception as err:
                print(f'Attempt {attempt + 1} failed:', err, self.response.json())
                if attempt < max_retries - 1:
                    print(f'Retrying in {wait_sec} seconds...')
                    time.sleep(wait_sec)
                else:
                    print('Max retries exceeded.')
                    raise
