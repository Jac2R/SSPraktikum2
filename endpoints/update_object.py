import requests
from endpoints.base_endpoint import BaseEndpoint

class UpdateEntity(BaseEndpoint):

    def update_by_id(self, entity_id, payload):
        self.response = requests.patch(
            f'http://localhost:8080/api/patch/{entity_id}',
            json=payload
        )

    def response_updated_id(self):
        updated_id = int(self.response.text)
        return updated_id