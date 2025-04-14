import io
import pytest
from src.currency_converter import CurrencyConverter


@pytest.fixture
def mock_csv_data():
    return """currency,rate
USD,1.0
EUR,0.85
GBP,0.75"""


def test_currency_converter(mock_csv_data):
    converter = CurrencyConverter()
    converter.load_rates(io.StringIO(mock_csv_data))
    assert converter.convert(100, "USD", "EUR") == 85.0


def test_invalid_currency(mock_csv_data):
    converter = CurrencyConverter()
    converter.load_rates(io.StringIO(mock_csv_data))
    with pytest.raises(ValueError, match="Invalid currency"):
        converter.convert(100, "USD", "XYZ")
