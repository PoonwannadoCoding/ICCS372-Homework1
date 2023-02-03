import requests


def test_create_stock():
    url = "http://127.0.0.1:5000/add/stock"
    data = {
        "name": "test_item_01",
        "items": 1,
        "machine_id": 1}
    response = requests.post(url, json=data)

    assert response.status_code == 200

def test_create_stock_cannot_find_id():
    url = "http://127.0.0.1:5000/add/stock"
    data = {
        "name": "test_item_01",
        "items": 1,
        "machine_id": 0}
    response = requests.post(url, json=data)
    # print(response)

    assert response.text == '{"error":"Machine ID does not exist"}\n'

