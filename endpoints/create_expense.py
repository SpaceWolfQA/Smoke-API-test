import pytest
import requests
import time

from config.settings import set, get
from endpoints.base_endpoint import Endpoint


class CreateExpense(Endpoint):

    def create_expense(self, url_bill, headers, payload, max_retries, wait_sec):
        for attempt in range(max_retries):
            try:
                self.response = requests.post(f'{url_bill}/v3/expenses', headers=headers, json=payload)
                self.response.raise_for_status()
                expense_id = self.response.json()['id']
                money_value = self.response.json()['money_value']
                set('expense_id', expense_id)
                set('money_value', money_value)
                print('Response Status Code:', self.response.status_code)
                break

            except Exception as err:
                print(f'Attempt {attempt + 1} failed:', err, self.response.json())
                if attempt < max_retries - 1:
                    print(f'Retrying in {wait_sec} seconds...')
                    time.sleep(wait_sec)
                else:
                    print('Max retries exceeded')
                    raise

    def check_create(self, url_bill, headers):
        expense_id = get('expense_id')
        expense_addendum_id = get('addendum_id')
        self.response = requests.get(f'{url_bill}/v3/expenses/{expense_id}', headers=headers)
        plan_item_id = self.response.json()['plan_item_id']
        addendum_id = self.response.json()['addendum_id']
        if plan_item_id != 387487 and expense_addendum_id != addendum_id:
            pytest.fail('Expense does not created')
        print('Expense created')
