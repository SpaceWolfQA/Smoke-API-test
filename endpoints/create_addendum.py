import pytest
import requests
import time

from config.settings import set, get
from endpoints.base_endpoint import Endpoint


class CreateAddendum(Endpoint):

    def create_addendum(self, url_bill, headers, payload, max_retries, wait_sec):
        for attempt in range(max_retries):
            try:
                self.response = requests.post(f'{url_bill}/v3/admin/addendums', headers=headers, json=payload)
                self.response.raise_for_status()
                addendum_id = self.response.json()['id']
                set('addendum_id', addendum_id)
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

    def check_activate(self, url_bill, headers, max_retries, wait_sec):
        addendum_id = get('addendum_id')
        for attempt in range(max_retries):
            try:
                self.response = requests.get(f'{url_bill}/v3/admin/addendums/{addendum_id}', headers=headers)
                add_status = self.response.json()['status']
                if add_status == 'active':
                    print('Addendum activated')
                    break
                elif add_status == 'upcoming':
                    print('Addendum upcoming')
                else:
                    pytest.fail('Plan does not copied')
                if attempt < max_retries - 1:
                    print(f'Retrying in {wait_sec} seconds...')
                    time.sleep(wait_sec)

            except Exception as err:
                print(f'Attempt {attempt + 1} failed:', err, self.response.json())
                if attempt < max_retries - 1:
                    print(f'Retrying in {wait_sec} seconds...')
                    time.sleep(wait_sec)
                else:
                    print('Max retries exceeded')
                    raise
