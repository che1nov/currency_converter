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
