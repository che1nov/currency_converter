import pytest
from currency_converter import CurrencyConverter


@pytest.fixture
def converter():
    csv_content = "Currency,Rate\nUSD,1.0\nEUR,0.92\nGBP,0.79\nRUB,76.5"
    with open("test_rates.csv", "w", encoding="utf-8") as file:
        file.write(csv_content)
    return CurrencyConverter("test_rates.csv")


def test_convert(converter):
    assert converter.convert(100, "USD", "EUR") == 92.0
    assert converter.convert(50, "USD", "GBP") == 39.5


def test_invalid_currency(converter):
    with pytest.raises(ValueError):
        converter.convert(100, "USD", "XYZ")
