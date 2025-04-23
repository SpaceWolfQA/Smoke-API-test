import allure
import requests
import time

from endpoints.base_endpoint import Endpoint
from config.settings import get


class UpdateClient(Endpoint):

    def update_signup(self, url_iam, headers, payload, max_retries, wait_sec):
        with allure.step('Get client_id'):
            client_id = get('client_id')
        with allure.step('Update sign up'):
            for attempt in range(max_retries):
                try:
                    self.response = requests.put(f'{url_iam}/clients/{client_id}', headers=headers, json=payload)
                    self.response.raise_for_status()
                    break

                except Exception as err:
                    print(f'Attempt {attempt + 1} failed', err, self.response.json())
                    if attempt < max_retries - 1:
                        time.sleep(wait_sec)
                    else:
                        raise

    def cancel_recurring_payments(self, url_bill, headers, payload, max_retries, wait_sec):
        with allure.step('Get client_id'):
            client_id = get('client_id')
        with allure.step('Cancel requrring payments'):
            for attempt in range(max_retries):
                try:
                    self.response = requests.put(
                        f'{url_bill}/v1/clients/{client_id}/options',
                        headers=headers,
                        json=payload
                    )
                    self.response.raise_for_status()
                    break

                except Exception as err:
                    print(f'Attempt {attempt + 1} failed:', err, self.response.json())
                    if attempt < max_retries - 1:
                        time.sleep(wait_sec)
                    else:
                        raise

    def delete_yoomoney(self, url_bill, headers, max_retries, wait_sec):
        with allure.step('Get client_id'):
            client_id = get('client_id')
        with allure.step('Delete yoomoney payment method'):
            for attempt in range(max_retries):
                try:
                    self.response = requests.delete(
                        f'{url_bill}/v1/payment_methods/21/allowed/{client_id}',
                        headers=headers
                    )
                    self.response.raise_for_status()
                    break

                except Exception as err:
                    print(f'Attempt {attempt + 1} failed:', err, self.response.json())
                    if attempt < max_retries - 1:
                        time.sleep(wait_sec)
                    else:
                        raise

    def add_bank_transfer(self, url_bill, headers, payload, max_retries, wait_sec):
        with allure.step('Add bank transfer payment method'):
            for attempt in range(max_retries):
                try:
                    self.response = requests.post(
                        f'{url_bill}/v1/payment_methods/16/allowed',
                        headers=headers,
                        json=payload
                    )
                    self.response.raise_for_status()
                    break

                except Exception as err:
                    print(f'Attempt {attempt + 1} failed:', err, self.response.json())
                    if attempt < max_retries - 1:
                        time.sleep(wait_sec)
                    else:
                        raise

    def check_signup(self, url_iam, headers, max_retries, wait_sec):
        with allure.step('Get test variable (client_id)'):
            client_id = get('client_id')
        with allure.step('Check sign up'):
            for attempt in range(max_retries):
                try:
                    self.response = requests.get(f'{url_iam}/clients/{client_id}', headers=headers)
                    current_signup = self.response.json()['signup_process']
                    assert current_signup is None
                    break

                except Exception as err:
                    print(f'Attempt {attempt + 1} failed:', err, self.response.json())
                    if attempt < max_retries - 1:
                        time.sleep(wait_sec)
                    else:
                        raise

    def check_recurring_payments(self, url_bill, headers, max_retries, wait_sec):
        with allure.step('Get test variable (client_id)'):
            client_id = get('client_id')
        with allure.step('Check requrring payments status'):
            for attempt in range(max_retries):
                try:
                    self.response = requests.get(f'{url_bill}/v1/clients/{client_id}/options', headers=headers)
                    current_recurring_payments = self.response.json()['recurring_payments']
                    assert current_recurring_payments is False
                    break

                except Exception as err:
                    print(f'Attempt {attempt + 1} failed:', err, self.response.json())
                    if attempt < max_retries - 1:
                        time.sleep(wait_sec)
                    else:
                        raise

    def check_payments_methods(self, url_bill, headers, max_retries, wait_sec):
        with allure.step('Get test variable (client_id)'):
            client_id = get('client_id')
        with allure.step('Check current payment method'):
            for attempt in range(max_retries):
                try:
                    self.response = requests.get(f'{url_bill}/v1/payment_methods?client_id={client_id}', headers=headers)
                    payments_methods = self.response.json()
                    assert len(payments_methods) == 1 and payments_methods[0]['name'] == 'bank'
                    break

                except Exception as err:
                    print(f'Attempt {attempt + 1} failed:', err, self.response.json())
                    if attempt < max_retries - 1:
                        time.sleep(wait_sec)
                    else:
                        raise
