import pytest
import requests
import time

from config.settings import set, get
from endpoints.base_endpoint import Endpoint


class DeleteInvoiceItem(Endpoint):

    def get_invoice_item_id(self, url_bill, headers):
        invoice_id = get('invoice_id')
        self.response = requests.get(f'{url_bill}/v5/invoices/{invoice_id}/items', headers=headers)
        invoice_item_id = self.response.json()[0]['id']
        set('invoice_item_id', invoice_item_id)

    def delete_invoice_item(self, url_bill, headers, max_retries, wait_sec):
        invoice_id = get('invoice_id')
        invoice_item_id = get('invoice_item_id')
        for attempt in range(max_retries):
            try:
                self.response = requests.delete(
                    f'{url_bill}/v5/invoices/{invoice_id}/items/{invoice_item_id}',
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

    def check_deletion(self, url_bill, headers):
        invoice_item_id = get('invoice_item_id')
        self.response = requests.get(f'{url_bill}/v5/invoices/{invoice_item_id}', headers=headers)
        if self.response.status_code != 404:
            pytest.fail('Invoice item does not deleted')
        print('invoice item deleted')
