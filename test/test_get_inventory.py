import requests

url = "http://127.0.0.1:5000/get/machine/inventory"


def test_get_stock():
    data = {"id":1}
    response = requests.get(url, json = data)
    assert response.status_code == 200

