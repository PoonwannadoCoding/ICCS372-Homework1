import requests

url = "http://127.0.0.1:5000/get/all/machine"


def test_get_machine():
    response = requests.get(url)
    assert response.status_code == 200
