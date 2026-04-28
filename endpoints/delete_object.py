import requests
from endpoints.base_endpoint import BaseEndpoint

class DeleteEntity(BaseEndpoint):

    def delete_by_id(self, entity_id):
        self.response = requests.delete(f'http://localhost:8080/api/delete/{entity_id}')
