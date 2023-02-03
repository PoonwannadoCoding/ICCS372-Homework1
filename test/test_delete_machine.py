import requests

url_for_delete_machine = "http://127.0.0.1:5000/delete/machine"
url_for_create_machine = "http://127.0.0.1:5000/add/machine"


def test_create_machine():
    data = {
        "name": "test_vending_machine_01",
        "location": "test_location_01"
    }
    requests.post(url_for_create_machine, json=data)


def test_delete_machine():
    delete_data = {"id": 2}
    response = requests.delete(url_for_delete_machine,json = delete_data)
    assert response.status_code == 200


