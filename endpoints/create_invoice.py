import allure
import requests
import time

from config.settings import set, get
from endpoints.base_endpoint import Endpoint


class CreateInvoice(Endpoint):

    def create_invoice(self, url_bill, headers, payload, max_retries, wait_sec):
        with allure.step('Create invoice'):
            for attempt in range(max_retries):
                try:
                    self.response = requests.post(f'{url_bill}/v5/invoices', headers=headers, json=payload)
                    self.response.raise_for_status()
                    invoice_id = self.response.json()['id']
                    set('invoice_id', invoice_id)
                    break

                except Exception as err:
                    print(f'Attempt {attempt + 1} failed:', err, self.response.json())
                    if attempt < max_retries - 1:
                        time.sleep(wait_sec)
                    else:
                        raise

    def check_create(self, url_bill, headers, max_retries, wait_sec):
        with allure.step('Get test variables (invoice_id, invoice_payer_id, money_value)'):
            invoice_id = get('invoice_id')
            invoice_payer_id = get('payer_id')
            money_value = get('money_value')
        with allure.step('Check invoice creation'):
            for attempt in range(max_retries):
                try:
                    self.response = requests.get(f'{url_bill}/v5/invoices/{invoice_id}', headers=headers)
                    payer_id = self.response.json()['payer_id']
                    total_sum = self.response.json()['total_sum']
                    assert invoice_payer_id == payer_id and money_value == total_sum
                    break

                except Exception as err:
                    print(f'Attempt {attempt + 1} failed:', err, self.response.json())
                    if attempt < max_retries - 1:
                        time.sleep(wait_sec)
                    else:
                        raise
