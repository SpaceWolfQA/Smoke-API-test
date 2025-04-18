import pytest
import requests
import time

from config.settings import get
from endpoints.base_endpoint import Endpoint


class DeleteFeature(Endpoint):

    def delete_feature(self, url_bill, headers, max_retries, wait_sec):
        feature_id = get('feature_id')
        for attempt in range(max_retries):
            try:
                self.response = requests.delete(f'{url_bill}/v3/features/{feature_id}', headers=headers)
                self.response.raise_for_status()
                print('Response Status Code:', self.response.status_code)
                break

            except Exception as err:
                print(f'Attempt {attempt + 1} failed:', err)
                if attempt < max_retries - 1:
                    print(f'Retrying in {wait_sec} seconds...')
                    time.sleep(wait_sec)
                else:
                    print('Max retries exceeded')
                    raise

    def check_deletion(self, url_bill, headers, max_retries, wait_sec):
        feature_id = get('feature_id')
        for attempt in range(max_retries):
            try:
                self.response = requests.get(f'{url_bill}/v3/features/{feature_id}', headers=headers)
                if self.response.status_code != 404:
                    pytest.fail('Feature does not deleted')
                print('Feature deleted')
                break

            except Exception as err:
                print(f'Attempt {attempt + 1} failed:', err)
                if attempt < max_retries - 1:
                    print(f'Retrying in {wait_sec} seconds...')
                    time.sleep(wait_sec)
                else:
                    print('Max retries exceeded')
                    raise
