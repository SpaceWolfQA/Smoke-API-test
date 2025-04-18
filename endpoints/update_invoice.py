import pytest
import requests
import time

from config.settings import get
from endpoints.base_endpoint import Endpoint


class UpdateInvoice(Endpoint):

    def update_invoice(self, url_bill, headers, max_retries, wait_sec):
        invoice_id = get('invoice_id')
        for attempt in range(max_retries):
            try:
                self.response = requests.post(f'{url_bill}/v5/invoices/{invoice_id}/regenerate', headers=headers)
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

    def check_update(self, url_bill, headers, max_retries, wait_sec):
        invoice_id = get('invoice_id')
        invoice_payer_id = get('payer_id')
        money_value = get('money_value')
        for attempt in range(max_retries):
            try:
                self.response = requests.get(f'{url_bill}/v5/invoices/{invoice_id}', headers=headers)
                payer_id = self.response.json()['payer_id']
                sum_expenses = self.response.json()['sum_expenses']
                if invoice_payer_id != payer_id and money_value != sum_expenses:
                    pytest.fail('Invoice does not updated')
                print('Invoice updated')
                break

            except Exception as err:
                print(f'Attempt {attempt + 1} failed:', err, self.response.json())
                if attempt < max_retries - 1:
                    print(f'Retrying in {wait_sec} seconds...')
                    time.sleep(wait_sec)
                else:
                    print('Max retries exceeded.')
                    raise
