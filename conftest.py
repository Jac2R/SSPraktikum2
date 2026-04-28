import pytest
from endpoints.create_object import CreateEntity
from endpoints.delete_object import DeleteEntity

@pytest.fixture(scope="function")
def ent_id():
    create_entity = CreateEntity()
    payload = {
        "addition": {
            "additional_info": "Дополнительные сведения",
            "additional_number": 123
        },
        "important_numbers": [
            42,
            87,
            15
        ],
        "title": "Основная сущность в Python",
        "verified": True
    }
    create_entity.new_entity(payload)
    entity_id = create_entity.response_obj_id()

    yield entity_id

    delete_entity = DeleteEntity()
    delete_entity.delete_by_id(entity_id)