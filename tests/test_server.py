import threading
import time

import pytest
import requests

from server import PORT, CurrencyConverterHandler, HTTPServer


# Фикстура для запуска сервера
@pytest.fixture(scope="session", autouse=True)
def start_server():
    """Запускает сервер в фоновом потоке."""

    def run_server():
        with HTTPServer(("", PORT), CurrencyConverterHandler) as httpd:
            httpd.serve_forever()

    # Запуск сервера в отдельном потоке
    server_thread = threading.Thread(target=run_server, daemon=True)
    server_thread.start()
    time.sleep(1)  # Ждем, пока сервер запустится


def test_get_operations(start_server):
    response = requests.get(f"http://localhost:{PORT}/operations")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_post_convert(start_server):
    payload = {"amount": 100, "from_currency": "USD", "to_currency": "EUR"}
    response = requests.post(
        f"http://localhost:{PORT}/convert",
        json=payload,
        headers={"Content-Type": "application/json"},
    )
    assert response.status_code == 200
    data = response.json()
    assert "converted_amount" in data
    assert data["from_currency"] == "USD"
    assert data["to_currency"] == "EUR"
