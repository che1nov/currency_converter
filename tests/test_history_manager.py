from history_manager import HistoryManager


def test_add_and_get_operations():
    manager = HistoryManager()
    operation = {
        "amount": 100,
        "from_currency": "USD",
        "to_currency": "EUR",
        "converted_amount": 92.0,
    }
    manager.add_operation(operation)
    assert manager.get_operations() == [operation]


def test_empty_history():
    manager = HistoryManager()
    assert manager.get_operations() == []
