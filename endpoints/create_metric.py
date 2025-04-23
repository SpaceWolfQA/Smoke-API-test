import allure
import requests
import time

from config.settings import set, get
from endpoints.base_endpoint import Endpoint


class CreateMetric(Endpoint):

    def create_metric(self, url_bill, headers, payload, max_retries, wait_sec):
        with allure.step('Create metric'):
            for attempt in range(max_retries):
                try:
                    self.response = requests.post(f'{url_bill}/v3/statistics/metrics', headers=headers, json=payload)
                    self.response.raise_for_status()
                    metric_id = self.response.json()['id']
                    set('metric_id', metric_id)
                    break

                except Exception as err:
                    print(f'Attempt {attempt + 1} failed:', err, self.response.json())
                    if attempt < max_retries - 1:
                        time.sleep(wait_sec)
                    else:
                        raise

    def check_create(self, url_bill, headers, max_retries, wait_sec):
        with allure.step('Get test variables (metric_id, metric_name)'):
            metric_id = get('metric_id')
            metric_name = get('metric_name')
        with allure.step('Check metric creation'):
            for attempt in range(max_retries):
                try:
                    self.response = requests.get(f'{url_bill}/v3/statistics/metrics/{metric_id}', headers=headers)
                    created_metric_name = self.response.json()['int_name']
                    assert created_metric_name == metric_name
                    break

                except Exception as err:
                    print(f'Attempt {attempt + 1} failed:', err, self.response.json())
                    if attempt < max_retries - 1:
                        time.sleep(wait_sec)
                    else:
                        raise
