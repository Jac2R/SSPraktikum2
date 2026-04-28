import requests
from endpoints.base_endpoint import BaseEndpoint

class CreateEntity(BaseEndpoint):

    def new_entity(self, payload):
        self.response = requests.post(
            'http://localhost:8080/api/create',
            json=payload
        )

    def response_obj_id(self):
        obj_id = int(self.response.text.strip())
        return obj_id
