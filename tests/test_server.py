# tests/test_server.py
import requests

BASE_URL = "http://localhost:8008"

def test_get_items():
    """Тест получения списка всех элементов."""
    response = requests.get(f"{BASE_URL}/items/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_item():
    """Тест создания нового элемента."""
    new_item = {"name": "Test Item", "value": 42}
    response = requests.post(f"{BASE_URL}/items/", json=new_item)
    assert response.status_code == 201
    assert response.json()["name"] == new_item["name"]
    assert response.json()["value"] == new_item["value"]

def test_get_item_by_id():
    """Тест получения элемента по ID."""
    item_id = 1  # Предполагаем, что такой элемент существует
    response = requests.get(f"{BASE_URL}/items/{item_id}/")
    assert response.status_code == 200
    assert response.json()["id"] == item_id

def test_update_item():
    """Тест обновления элемента."""
    item_id = 1  # Предполагаем, что такой элемент существует
    updated_data = {"name": "Updated Item", "value": 100}
    response = requests.put(f"{BASE_URL}/items/{item_id}/", json=updated_data)
    assert response.status_code == 200
    assert response.json()["name"] == updated_data["name"]
    assert response.json()["value"] == updated_data["value"]

def test_delete_item():
    """Тест удаления элемента."""
    item_id = 1  # Предполагаем, что такой элемент существует
    response = requests.delete(f"{BASE_URL}/items/{item_id}/")
    assert response.status_code == 204
