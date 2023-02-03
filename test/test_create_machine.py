import requests

url = "http://127.0.0.1:5000/add/machine"


def test_create_machine():
    data = {
        "name": "test_vending_machine_01",
        "location": "test_location_01"
    }
    response = requests.post(url, json=data)

    assert response.status_code == 200
