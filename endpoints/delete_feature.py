import allure
import requests
import time

from config.settings import get
from endpoints.base_endpoint import Endpoint


class DeleteFeature(Endpoint):

    def delete_feature(self, url_bill, headers, max_retries, wait_sec):
        with allure.step('Get feature_id'):
            feature_id = get('feature_id')
        with allure.step('Delete feature'):
            for attempt in range(max_retries):
                try:
                    self.response = requests.delete(f'{url_bill}/v3/features/{feature_id}', headers=headers)
                    self.response.raise_for_status()
                    break

                except Exception as err:
                    print(f'Attempt {attempt + 1} failed:', err)
                    if attempt < max_retries - 1:
                        time.sleep(wait_sec)
                    else:
                        raise

    def check_deletion(self, url_bill, headers, max_retries, wait_sec):
        with allure.step('Get test variable (feature_id)'):
            feature_id = get('feature_id')
        with allure.step('Check feature deletion'):
            for attempt in range(max_retries):
                try:
                    self.response = requests.get(f'{url_bill}/v3/features/{feature_id}', headers=headers)
                    assert self.response.status_code == 404
                    break

                except Exception as err:
                    print(f'Attempt {attempt + 1} failed:', err, self.response.json())
                    if attempt < max_retries - 1:
                        time.sleep(wait_sec)
                    else:
                        raise
