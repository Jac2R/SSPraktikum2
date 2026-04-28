import requests
from endpoints.base_endpoint import BaseEndpoint
from models.entity import Entity

class GetEntity(BaseEndpoint):

    def get_by_id(self, obj_id):
        self.response = requests.get(f'http://localhost:8080/api/get/{obj_id}')

    def response_ent_object(self):
        self.response_json = Entity(**self.response.json())
        return self.response_json

    def check_response_id(self, entity_id):
        assert self.response_json.id == entity_id