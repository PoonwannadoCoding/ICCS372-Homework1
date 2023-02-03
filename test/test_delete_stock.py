import requests

url_for_delete_stok = "http://127.0.0.1:5000/delete/stock"
url_for_create_stock = "http://127.0.0.1:5000/add/stock"
def test_create_stock():
    data = {
        "name": "test_item_01",
        "items": 1,
        "machine_id": 3}
    requests.post(url_for_create_stock, json=data)

def test_delete_stock():
    delete_data = {"id": 1}
    response = requests.delete(url_for_delete_stok, json=delete_data)
    assert response.status_code == 200
