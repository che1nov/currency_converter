from ..history_manager import HistoryManager
import pytest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


@pytest.fixture
def history_manager():
    return HistoryManager()


def test_add_operation(history_manager):
    # Тест на добавление операции
    operation = {
        "amount": 100,
        "from_currency": "USD",
        "to_currency": "EUR",
        "converted_amount": 92.0,
    }
    history_manager.add_operation(operation)
    assert history_manager.get_operations() == [operation]


def test_get_operations_empty(history_manager):
    # Тест на получение пустой истории
    assert history_manager.get_operations() == []


def test_get_operations_multiple(history_manager):
    # Тест на получение нескольких операций
    operation1 = {
        "amount": 100,
        "from_currency": "USD",
        "to_currency": "EUR",
        "converted_amount": 92.0,
    }
    operation2 = {
        "amount": 50,
        "from_currency": "EUR",
        "to_currency": "GBP",
        "converted_amount": 41.58,
    }
    history_manager.add_operation(operation1)
    history_manager.add_operation(operation2)
    assert history_manager.get_operations() == [operation1, operation2]
