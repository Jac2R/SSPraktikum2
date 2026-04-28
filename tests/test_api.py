from endpoints.create_object import CreateEntity
from endpoints.delete_object import DeleteEntity
from endpoints.get_all_objs import GetEntities
from endpoints.get_object import GetEntity
from endpoints.update_object import UpdateEntity


def test_create_entity():
    create_endpoint = CreateEntity()
    payload = {
            "addition": {
                "additional_info": "Дополнительные сведения",
                "additional_number": 321
            },
            "important_numbers": [
                428,
                871,
                154
            ],
            "title": "Создаваемая сущность в Python",
            "verified": True
    }
    create_endpoint.new_entity(payload)
    create_endpoint.check_status_code(200)
    entity_id = create_endpoint.response_obj_id()
    print("\nObject_id : ", entity_id)

    get_ent_endpoint = GetEntity()
    get_ent_endpoint.get_by_id(entity_id)
    create_data = get_ent_endpoint.response_ent_object()
    print("\nPOST :\n", create_data)

    delete_ent_endpoint = DeleteEntity()
    delete_ent_endpoint.delete_by_id(entity_id)


def test_get_entity(ent_id):
    get_ent_endpoint = GetEntity()
    get_ent_endpoint.get_by_id(ent_id)
    get_ent_endpoint.check_status_code(200)
    entity_data = get_ent_endpoint.response_ent_object()
    print("\nGET :\n", entity_data)
    get_ent_endpoint.check_response_id(ent_id)


def test_update_entity(ent_id):
    update_ent_endpoint = UpdateEntity()
    get_ent_endpoint = GetEntity()
    payload = {
        "addition": {
            "additional_info": "Иные сведения",
            "additional_number": 356
        },
        "important_numbers": [
            4,
            8,
            1
        ],
        "title": "Измененная сущность в Python",
        "verified": False
    }
    update_ent_endpoint.update_by_id(ent_id, payload=payload)
    update_ent_endpoint.check_status_code(204)
    get_ent_endpoint.get_by_id(ent_id)
    updated_data = get_ent_endpoint.response_ent_object()
    print("\nPATCH :\n", updated_data)


def test_get_all_entities():
    create_endpoint = CreateEntity()
    payload_1 = {
        "addition": {
            "additional_info": "Первые сведения",
            "additional_number": 111
        },
        "important_numbers": [
            42,
            87,
            15
        ],
        "title": "Первая сущность в Python",
        "verified": True
    }
    payload_2 = {
        "addition": {
            "additional_info": "Вторые сведения",
            "additional_number": 222
        },
        "important_numbers": [
            15,
            42,
            87
        ],
        "title": "Вторая сущность в Python",
        "verified": False
    }
    create_endpoint.new_entity(payload_1)
    entity_id_1 = create_endpoint.response_obj_id()
    create_endpoint.new_entity(payload_2)
    entity_id_2 = create_endpoint.response_obj_id()

    get_all_endpoint = GetEntities()
    get_all_endpoint.get_all()
    get_all_endpoint.check_status_code(200)

    all_entities = get_all_endpoint.response_ent_objects()
    print("\nGET All :\n", all_entities)

    ids = [entity.id for entity in all_entities]
    assert entity_id_1 in ids
    assert entity_id_2 in ids

    delete_ent_endpoint = DeleteEntity()
    delete_ent_endpoint.delete_by_id(entity_id_1)
    delete_ent_endpoint.delete_by_id(entity_id_2)

def test_delete_entity(ent_id):
    delete_ent_endpoint = DeleteEntity()
    get_ent_endpoint = GetEntity()
    delete_ent_endpoint.delete_by_id(ent_id)
    delete_ent_endpoint.check_status_code(204)
    get_ent_endpoint.get_by_id(ent_id)
    get_ent_endpoint.check_status_code(500)