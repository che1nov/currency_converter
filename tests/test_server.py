import threading
import time

import pytest
import requests

from server import CurrencyConverterHandler, HTTPServer


# Фикстура для запуска сервера на случайном свободном порту
@pytest.fixture(scope="session")
def free_port():
    """Находит свободный порт для сервера."""
    import socket

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("", 0))
        return s.getsockname()[1]


@pytest.fixture(scope="session", autouse=True)
def start_server(free_port):
    """Запускает сервер на свободном порту."""

    def run_server():
        with HTTPServer(("", free_port), CurrencyConverterHandler) as httpd:
            httpd.serve_forever()

    # Запуск сервера в отдельном потоке
    server_thread = threading.Thread(target=run_server, daemon=True)
    server_thread.start()
    time.sleep(1)  # Ждем, пока сервер запустится
    return free_port


def test_get_operations(start_server):
    response = requests.get(f"http://localhost:{start_server}/operations")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_post_convert(start_server):
    payload = {"amount": 100, "from_currency": "USD", "to_currency": "EUR"}
    response = requests.post(
        f"http://localhost:{start_server}/convert",
        json=payload,
        headers={"Content-Type": "application/json"},
    )
    assert response.status_code == 200
    data = response.json()
    assert "converted_amount" in data
    assert data["from_currency"] == "USD"
    assert data["to_currency"] == "EUR"
