import allure
import requests
import time

from config.settings import get
from endpoints.base_endpoint import Endpoint


class DeleteMetric(Endpoint):

    def delete_metric(self, url_bill, headers, max_retries, wait_sec):
        with allure.step('Get metric_id'):
            metric_id = get('metric_id')
        with allure.step('Delete metric'):
            for attempt in range(max_retries):
                try:
                    self.response = requests.delete(f'{url_bill}/v3/statistics/metrics/{metric_id}', headers=headers)
                    self.response.raise_for_status()
                    break

                except Exception as err:
                    print(f'Attempt {attempt + 1} failed:', err)
                    if attempt < max_retries - 1:
                        time.sleep(wait_sec)
                    else:
                        raise

    def check_deletion(self, url_bill, headers, max_retries, wait_sec):
        with allure.step('Get test variable (metric_id)'):
            metric_id = get('metric_id')
        with allure.step('Check metric deletion'):
            for attempt in range(max_retries):
                try:
                    self.response = requests.get(f'{url_bill}/v3/statistics/metrics/{metric_id}', headers=headers)
                    assert self.response.status_code == 404
                    break

                except Exception as err:
                    print(f'Attempt {attempt + 1} failed:', err)
                    if attempt < max_retries - 1:
                        time.sleep(wait_sec)
                    else:
                        raise
