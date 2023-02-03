import requests

url_for_edit_stock = "http://127.0.0.1:5000/edit/stock"

url_for_create_stock = "http://127.0.0.1:5000/add/stock"
def test_create_stock():
    data = {
        "name": "test_item_01",
        "items": 1,
        "machine_id": 3}
    requests.post(url_for_create_stock, json=data)

def test_edit_stock():
    data = {
        "id": 1,
        "name": "soap",
        "items": 20,
        "machine_id": 2
    }

    response = requests.put(url_for_edit_stock, json=data)
    assert response.status_code == 200

#
# def test_edit_stock_missing_id():
#     data = {
#         "name": "soap",
#         "items": 20,
#         "machine_id": 1
#     }
#
#     response = requests.put(url_for_edit_stock, json=data)
#     assert response.status_code == 500
#
#
# def test_edit_stock_missing_name():
#     data = {
#         "id": 1,
#         "items": 20,
#         "machine_id": 1
#     }
#
#     response = requests.put(url_for_edit_stock, json=data)
#     assert response.status_code == 500
#
#
# def test_edit_stock_missing_items():
#     data = {
#         "id": 1,
#         "name": "soap",
#         "machine_id": 1
#     }
#
#     response = requests.put(url_for_edit_stock, json=data)
#     assert response.status_code == 500
#
#
# def test_edit_stock_missing_machind_id():
#     data = {
#         "id": 1,
#         "name": "soap",
#         "items": 20
#     }
#
#     response = requests.put(url_for_edit_stock, json=data)
#     assert response.status_code == 500
