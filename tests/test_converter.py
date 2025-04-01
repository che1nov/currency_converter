import json
import os

import pytest

from converter import CurrencyConverter


@pytest.fixture
def converter():
    """Фикстура для создания экземпляра CurrencyConverter."""
    return CurrencyConverter(
        currencies_file="./currencies.csv", operations_file="./operations.json"
    )


@pytest.fixture
def cleanup_files():
    """Фикстура для очистки тестовых файлов перед выполнением тестов."""
    # Удаляем файл operations.json, если он существует
    if os.path.exists("tests/operations.json"):
        os.remove("tests/operations.json")
    yield
    # Очищаем файл operations.json после выполнения тестов
    if os.path.exists("tests/operations.json"):
        os.remove("tests/operations.json")


def test_load_currencies(converter):
    """Тест загрузки курсов валют."""
    rates = converter.rates
    assert rates == {"USD": 1.0, "EUR": 0.92, "GBP": 0.78}


def test_convert_currency_success(converter, cleanup_files):
    """Тест успешной конвертации валют."""
    result = converter.convert_currency(100, "USD", "EUR")
    assert result == 92.0

    # Проверяем, что операция записана в историю
    operations = converter.get_operations_history()
    assert operations[0]["amount"] == 100
    assert operations[0]["from_currency"] == "USD"
    assert operations[0]["to_currency"] == "EUR"
    assert operations[0]["result"] == 92.0


def test_convert_currency_invalid_currency(converter):
    """Тест конвертации с недопустимой валютой."""
    with pytest.raises(ValueError, match="Курс для валюты XYZ или EUR не найден."):
        converter.convert_currency(100, "XYZ", "EUR")


def test_save_operations(converter, cleanup_files):
    """Тест сохранения операций."""
    operations = [
        {"amount": 100, "from_currency": "USD", "to_currency": "EUR", "result": 92.0}
    ]
    converter.operations = operations
    converter.save_operations()

    # Проверяем, что файл сохранен корректно
    with open("./operations.json", "r", encoding="utf-8") as file:
        saved_operations = json.load(file)
    assert saved_operations == operations


def test_get_operations_history(converter, cleanup_files):
    """Тест получения истории операций."""
    converter.convert_currency(100, "USD", "EUR")
    history = converter.get_operations_history()
    assert history[0]["amount"] == 100
    assert history[0]["from_currency"] == "USD"
    assert history[0]["to_currency"] == "EUR"
    assert history[0]["result"] == 92.0
