import requests

BASE_URL = "http://localhost"
PORT = 8008


def send_post_request(path, data):
    url = f"{BASE_URL}: {PORT}{path}"
    response = requests.post(url, json=data)
    return response.json()


def send_get_request(path):
    url = f"{BASE_URL}: {PORT}{path}"
    response = requests.get(url)
    return response.json()


def test_convert_currency(setup_server):
    url = f"{BASE_URL}: {PORT}/convert"
    data = {"amount": 100, "from": "USD", "to": "EUR"}
    response = requests.post(url, json=data)
    response_data = response.json()
    assert "result" in response_data
    assert response_data["result"] == 85.0


def test_get_history(setup_server):
    url = f"{BASE_URL}: {PORT}/history"
    response = requests.get(url)
    response_data = response.json()
    assert "history" in response_data
