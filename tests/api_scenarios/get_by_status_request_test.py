import requests
import configparser
import pytest

config = configparser.ConfigParser()
config.read('config.ini')
petstore_url = config['Petstore']['url']
FIND_BY_STATUS = petstore_url + '/pet/findByStatus?status='
GET_SINGLE_PET = petstore_url + '/pet/'

statuses = ['available', 'pending', 'sold']


@pytest.mark.parametrize('stat ', statuses)
def test_first_request_findByStatus(stat):
    response = requests.get(FIND_BY_STATUS + stat)
    assert response.status_code == 200
    assert len(response.json()) != 0
    print(response.json())
    for animal in response.json():
        assert animal['status'] == stat


@pytest.mark.parametrize('pet_id', [1, 2, 5, 4, 2, 1, 2, 10])
def test_get_single_pet(pet_id):
    response = requests.get(GET_SINGLE_PET + (str(pet_id)))
    assert response.status_code == 200
    assert len(response.json()) != 0
    assert response.json()['id'] == pet_id
    print(response.json())
