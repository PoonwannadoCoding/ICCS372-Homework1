import requests

url = "http://127.0.0.1:5000/get/all/stock"


def test_get_stock():
    response = requests.get(url)
    assert response.status_code == 200
