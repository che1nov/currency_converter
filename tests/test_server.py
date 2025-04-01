import requests
from server import PORT

def test_get_operations():
    response = requests.get(f"http://localhost:{PORT}/operations")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_post_convert():
    payload = {
        "amount": 100,
        "from_currency": "USD",
        "to_currency": "EUR"
    }
    response = requests.post(
        f"http://localhost:{PORT}/convert",
        json=payload,
        headers={"Content-Type": "application/json"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "converted_amount" in data
    assert data["from_currency"] == "USD"
    assert data["to_currency"] == "EUR"

    invalid_payload = {
        "amount": "invalid",
        "from_currency": "USD",
        "to_currency": "EUR"
    }
    response = requests.post(
        f"http://localhost:{PORT}/convert",
        json=invalid_payload,
        headers={"Content-Type": "application/json"}
    )
    assert response.status_code == 400
    