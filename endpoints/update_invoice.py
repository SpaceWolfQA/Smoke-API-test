import allure
import requests
import time

from config.settings import get
from endpoints.base_endpoint import Endpoint


class UpdateInvoice(Endpoint):

    def update_invoice(self, url_bill, headers, max_retries, wait_sec):
        with allure.step('Get invoice_id'):
            invoice_id = get('invoice_id')
        with allure.step('Update invoice'):
            for attempt in range(max_retries):
                try:
                    self.response = requests.post(f'{url_bill}/v5/invoices/{invoice_id}/regenerate', headers=headers)
                    self.response.raise_for_status()
                    break

                except Exception as err:
                    print(f'Attempt {attempt + 1} failed:', err, self.response.json())
                    if attempt < max_retries - 1:
                        time.sleep(wait_sec)
                    else:
                        raise

    def check_update(self, url_bill, headers, max_retries, wait_sec):
        with allure.step('Get test variables (invoice_id, invoice_payer_id, sum_money_value)'):
            invoice_id = get('invoice_id')
            invoice_payer_id = get('payer_id')
            sum_money_value = get('sum_money_value')
        with allure.step('Check invoice update'):
            for attempt in range(max_retries):
                try:
                    self.response = requests.get(f'{url_bill}/v5/invoices/{invoice_id}', headers=headers)
                    payer_id = self.response.json()['payer_id']
                    sum_expenses = self.response.json()['sum_expenses']
                    assert invoice_payer_id == payer_id and sum_money_value == sum_expenses
                    break

                except Exception as err:
                    print(f'Attempt {attempt + 1} failed:', err, self.response.json())
                    if attempt < max_retries - 1:
                        time.sleep(wait_sec)
                    else:
                        raise
