import pytest
import requests
import time

from config.settings import get
from endpoints.base_endpoint import Endpoint


class EditFeature(Endpoint):

    def edit_feature(self, url_bill, headers, payload, max_retries, wait_sec):
        feature_id = get('feature_id')
        for attempt in range(max_retries):
            try:
                self.response = requests.put(f'{url_bill}/v3/features/{feature_id}', headers=headers, json=payload)
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

    def check_edit(self, url_bill, headers, max_retries, wait_sec):
        feature_id = get('feature_id')
        feature_name = get('edit_feature_name_en')
        for attempt in range(max_retries):
            try:
                self.response = requests.get(f'{url_bill}/v3/features/{feature_id}', headers=headers)
                create_feature_name = self.response.json()['name_en']
                if feature_name != create_feature_name:
                    pytest.fail(f'Feature does not edit, response: {self.response.json()}')
                print('Feature edited')
                break

            except Exception as err:
                print(f'Attempt {attempt + 1} failed:', err, self.response.json())
                if attempt < max_retries - 1:
                    print(f'Retrying in {wait_sec} seconds...')
                    time.sleep(wait_sec)
                else:
                    print('Max retries exceeded.')
                    raise
