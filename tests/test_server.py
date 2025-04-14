import requests

BASE_URL = "http://localhost:8008"


def test_convert_currency():
    url = f"{BASE_URL}/convert"
    data = {"amount": 100, "from": "USD", "to": "EUR"}
    response = requests.post(url, json=data)
    assert response.status_code == 200
    result = response.json()
    assert "amount" in result
    assert "from" in result
    assert "to" in result
    assert "result" in result
    assert result["result"] == 85.0


def test_get_history():
    url = f"{BASE_URL}/history"
    response = requests.get(url)
    assert response.status_code == 200
    result = response.json()
    assert "history" in result
    assert isinstance(result["history"], list)
