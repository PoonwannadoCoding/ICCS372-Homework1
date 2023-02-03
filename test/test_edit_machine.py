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
#
#
# def test_edit_machine_missing_id():
#     data = {
#         "name": "test_edit_item_01",
#         "location": "test_edit_location_01"
#     }
#     response = requests.put(url, json=data)
#
#     assert response.status_code == 500
#
#
# def test_edit_machine_missing_name():
#     data = {
#         "id": 1,
#         "location": "test_edit_location_01"
#     }
#     response = requests.put(url, json=data)
#
#     assert response.status_code == 500
#
#
# def test_edit_machine_missing_location():
#     data = {
#         "id": 4,
#         "name": "test_edit_item_01"
#     }
#     response = requests.put(url, json=data)
#
#     assert response.status_code == 500
#
#
# def test_edit_machine_missing_all_information():
#     data = {}
#     response = requests.put(url, json=data)
#
#     assert response.status_code == 500
