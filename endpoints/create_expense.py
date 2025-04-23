import allure
import requests
import time

from config.settings import set, get
from endpoints.base_endpoint import Endpoint


class CreateExpense(Endpoint):

    def create_expense(self, url_bill, headers, payload, max_retries, wait_sec):
        with allure.step('Create expense'):
            money_value = get('money_value')
            for attempt in range(max_retries):
                try:
                    self.response = requests.post(f'{url_bill}/v3/expenses', headers=headers, json=payload)
                    self.response.raise_for_status()
                    expense_id = self.response.json()['id']
                    second_money_value = self.response.json()['money_value']
                    sum_money_value = f'{float(money_value) + float(second_money_value):.2f}'
                    set('expense_id', expense_id)
                    set('sum_money_value', sum_money_value)
                    break

                except Exception as err:
                    print(f'Attempt {attempt + 1} failed:', err, self.response.json())
                    if attempt < max_retries - 1:
                        time.sleep(wait_sec)
                    else:
                        raise

    def check_create(self, url_bill, headers, max_retries, wait_sec):
        with allure.step('Get test variables (expense_id, expense_addendum_id)'):
            expense_id = get('expense_id')
            expense_addendum_id = get('addendum_id')
        with allure.step('Check expense creation'):
            for attempt in range(max_retries):
                try:
                    self.response = requests.get(f'{url_bill}/v3/expenses/{expense_id}', headers=headers)
                    plan_item_id = self.response.json()['plan_item_id']
                    addendum_id = self.response.json()['addendum_id']
                    assert plan_item_id == 387487 and expense_addendum_id == addendum_id
                    break

                except Exception as err:
                    print(f'Attempt {attempt + 1} failed:', err, self.response.json())
                    if attempt < max_retries - 1:
                        time.sleep(wait_sec)
                    else:
                        raise
