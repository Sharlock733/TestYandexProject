import pytest
import requests
import configparser
import json

config = configparser.ConfigParser()
config.read('config.ini')
petstore_url = config['Petstore']['url']

STORE_ORDER_URL = petstore_url + '/store/order'


@pytest.mark.parametrize('json_file', ['tests/utils/json_body/post_request_for_order_pet_body.json',
                                       'tests/utils/json_body/post_request_for_order_pet_body2.json'])
def test_post_request_for_order_pet(json_file):
    with open(json_file) as f:
        body = json.load(f)
    response = requests.post(
        STORE_ORDER_URL,
        json=body,
        headers={'accept': 'application/json', 'Content-Type': 'application/json'})
    assert response.status_code == 200
    assert len(response.json()) != 0
    assert response.json()['id'] == body['id']
    assert response.json()['petId'] == body['petId']
    assert response.json()['quantity'] == body['quantity']
    assert response.json()['status'] == body['status']
    print(response.json())
