class BaseEndpoint:
    response = None
    response_json = None
    ent_id = None

    def check_status_code(self, expected_status):
        assert self.response.status_code == expected_status