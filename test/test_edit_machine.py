import requests

url = "http://127.0.0.1:5000/edit/machine"


def test_edit_machine():
    data = {
        "id": 6,
        "name": "test_edit_item_01",
        "location": "test_edit_location_01"
    }
    response = requests.put(url, json=data)

    assert response.status_code == 200
