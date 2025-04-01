import csv

from server import convert_currency, load_currencies, load_operations, save_operations


def test_load_currencies(tmp_path):
    file = tmp_path / "currencies.csv"
    with open(file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["currency", "rate"])
        writer.writeheader()
        writer.writerow({"currency": "USD", "rate": "1.0"})
        writer.writerow({"currency": "EUR", "rate": "0.92"})

    rates = load_currencies(file)
    assert rates == {"USD": 1.0, "EUR": 0.92}

    assert load_currencies("nonexistent.csv") == {}


def test_save_and_load_operations(tmp_path):
    file = tmp_path / "operations.json"

    operations = [
        {"amount": 100, "from_currency": "USD", "to_currency": "EUR", "result": 92.0}
    ]
    save_operations(operations, file)

    loaded_operations = load_operations(file)
    assert loaded_operations == operations

    assert load_operations("nonexistent.json") == []


def test_convert_currency():
    rates = {
        "USD": 1.0,
        "EUR": 0.92,
        "GBP": 0.78,
    }

    assert convert_currency(100, "USD", "EUR", rates) == 92.0
    assert convert_currency(50, "EUR", "GBP", rates) == 42.39
    assert convert_currency(100, "USD", "USD", rates) == 100.0

    assert convert_currency(100, "USD", "XYZ", rates) is None
    assert convert_currency(100, "XYZ", "EUR", rates) is None
