import allure


class Endpoint:
    response = None

    def check_status_code_is_200(self):
        with allure.step('Check response status code is 200'):
            assert self.response.status_code == 200, 'Response Status Code: 200'

    def check_status_code_is_201(self):
        with allure.step('Check response status code is 201'):
            assert self.response.status_code == 201, 'Response Status Code: 201'

    def check_status_code_is_204(self):
        with allure.step('Check response status code is 204'):
            assert self.response.status_code == 204, 'Response Status Code: 204'
