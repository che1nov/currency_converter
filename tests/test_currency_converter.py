from ..currency_converter import CurrencyConverter
import pytest


@pytest.fixture
def converter():
    # Создаем временную CSV-строку для тестирования
    csv_content = "Currency,Rate\nUSD,1.0\nEUR,0.92\nGBP,0.79\nRUB,76.5"
    with open("test_rates.csv", "w", encoding="utf-8") as file:
        file.write(csv_content)
    return CurrencyConverter("test_rates.csv")


def test_convert_valid_currencies(converter):
    # Тест на корректную конвертацию
    assert converter.convert(100, "USD", "EUR") == 92.0
    assert converter.convert(50, "EUR", "GBP") == 42.93
    assert converter.convert(1000, "USD", "RUB") == 76500.0


def test_convert_same_currency(converter):
    # Тест на конвертацию одной валюты в ту же самую
    assert converter.convert(100, "USD", "USD") == 100.0
    assert converter.convert(50, "EUR", "EUR") == 50.0


def test_convert_invalid_currency(converter):
    # Тест на обработку недопустимых валют
    with pytest.raises(ValueError, match="Валюта не поддерживается."):
        converter.convert(100, "USD", "XYZ")
    with pytest.raises(ValueError, match="Валюта не поддерживается."):
        converter.convert(100, "XYZ", "EUR")


def test_load_rates_from_csv(converter):
    # Тест на корректное чтение курсов из CSV
    assert converter.rates["USD"] == 1.0
    assert converter.rates["EUR"] == 0.92
    assert converter.rates["GBP"] == 0.79
    assert converter.rates["RUB"] == 76.5
