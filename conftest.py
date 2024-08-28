import pytest
import requests
import random


@pytest.fixture(scope="session", autouse=True)
def base_url():
    base_url = "https://petstore.swagger.io/v2"
    return base_url


@pytest.fixture(scope="session", autouse=True)
def pet_id():
    pet_id = random.randint(1, 123454321)
    return pet_id


@pytest.fixture(scope="session", autouse=True)
def data(pet_id):
    data = {
        "id": pet_id,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "Peeesik",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }
    return data


@pytest.fixture(scope="session", autouse=True)
def update_pet_data(pet_id):
    update_pet_data = {
        "id": pet_id,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "Peeesik",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "booked"
    }
    return update_pet_data


@pytest.fixture(scope="session", autouse=True)
def setup(base_url, pet_id, data):
    create_pet = requests.post(f'{base_url}/pet', json=data)

    print('\nTest of create pet')
    print('Text: ' + create_pet.text)
    print('Status: ' + str(create_pet.status_code))
    assert create_pet.status_code == 200

    yield

    delete_pet = requests.delete(f'{base_url}/pet/{pet_id}')

    print('\nDelete pet')
    print('Text:' + delete_pet.text)
    print('Status: ' + str(delete_pet.status_code))
    assert delete_pet.status_code == 200
