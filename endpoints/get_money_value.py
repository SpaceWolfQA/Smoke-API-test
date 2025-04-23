import allure
import requests
import time

from config.settings import get, set
from endpoints.base_endpoint import Endpoint


class GetMoneyValue(Endpoint):

    def get_money_value(self, url_bill, headers, max_retries, wait_sec):
        with allure.step('Get client_id'):
            client_id = get('client_id')
        with allure.step('Get money value'):
            for attempt in range(max_retries):
                try:
                    self.response = requests.get(
                        f'{url_bill}/v3/expenses?offset=0&limit=10&ordering=-id&client_id={client_id}',
                        headers=headers
                    )
                    self.response.raise_for_status()
                    money_value = self.response.json()['results'][0]['money_value']
                    set('money_value', money_value)
                    break

                except Exception as err:
                    print(f'Attempt {attempt + 1} failed:', err, self.response.json())
                    if attempt < max_retries - 1:
                        time.sleep(wait_sec)
                    else:
                        raise
