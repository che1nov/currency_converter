import pytest
from currency_converter import CurrencyConverter


@pytest.fixture
def converter():
    return CurrencyConverter("data/exchange_rates.csv")


def test_convert(converter):
    assert converter.convert(100, "USD", "EUR") == 92.0
    assert converter.convert(50, "USD", "GBP") == pytest.approx(39.5)


def test_invalid_currency(converter):
    with pytest.raises(ValueError):
        converter.convert(100, "USD", "XYZ")
