import pytest
import requests
import time

from config.settings import set, get
from endpoints.base_endpoint import Endpoint


class CreateFeature(Endpoint):

    def create_feature(self, url_bill, headers, payload, max_retries, wait_sec):
        for attempt in range(max_retries):
            try:
                self.response = requests.post(f'{url_bill}/v3/features', headers=headers, json=payload)
                self.response.raise_for_status()
                feature_id = self.response.json()['id']
                set('feature_id', feature_id)
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

    def check_create(self, url_bill, headers):
        feature_id = get('feature_id')
        feature_name = get('create_feature_name_en')
        self.response = requests.get(f'{url_bill}/v3/features/{feature_id}', headers=headers)
        create_feature_name = self.response.json()['name_en']
        if feature_name != create_feature_name:
            pytest.fail('Feature does not created')
        print('Feature created')
