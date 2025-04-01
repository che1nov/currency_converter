import os
import json
from history_manager import HistoryManager


def test_add_and_get_operations(tmp_path):
    file_path = tmp_path / "test_operations.json"
    manager = HistoryManager(file_path=str(file_path))

    operation = {
        "amount": 100,
        "from_currency": "USD",
        "to_currency": "EUR",
        "converted_amount": 92.0,
    }
    manager.add_operation(operation)
    assert manager.get_operations() == [operation]


def test_empty_history(tmp_path):
    file_path = tmp_path / "test_operations.json"
    manager = HistoryManager(file_path=str(file_path))
    assert manager.get_operations() == []


def test_save_operations(tmp_path):
    # Создаем временный файл operations.json
    file_path = tmp_path / "test_operations.json"

    # Инициализируем менеджер истории
    manager = HistoryManager(file_path=str(file_path))
    operation = {
        "amount": 100,
        "from_currency": "USD",
        "to_currency": "EUR",
        "converted_amount": 92.0,
    }
    manager.add_operation(operation)

    # Проверяем, что файл создан и содержит корректные данные
    assert os.path.exists(file_path)
    with open(file_path, "r") as file:
        data = json.load(file)
        assert data == [operation]
