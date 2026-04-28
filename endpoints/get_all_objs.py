import requests
from endpoints.base_endpoint import BaseEndpoint
from models.entity import Entity

class GetEntities(BaseEndpoint):

    def get_all(self):
        self.response = requests.get('http://localhost:8080/api/getAll')

    def response_ent_objects(self):
        self.response_json = [
            Entity(**entity)
            for entity in self.response.json()["entity"]
        ]
        return self.response_json