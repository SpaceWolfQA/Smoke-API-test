class Endpoint:
    response = None

    def check_status_code_is_200(self):
        assert self.response.status_code == 200, 'Response Status Code: 200'

    def check_status_code_is_201(self):
        assert self.response.status_code == 201, 'Response Status Code: 201'

    def check_status_code_is_204(self):
        assert self.response.status_code == 204, 'Response Status Code: 204'
