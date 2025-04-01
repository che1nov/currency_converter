from unittest.mock import patch
from main import main


def test_main(capsys):
    # Мокаем print для проверки вывода
    with patch("builtins.print") as mock_print:
        main()

    # Проверяем, что print был вызван с ожидаемыми аргументами
    mock_print.assert_any_call("100 USD = 92.0 EUR")
    mock_print.assert_any_call(
        "History:",
        [
            {
                "amount": 100,
                "from_currency": "USD",
                "to_currency": "EUR",
                "converted_amount": 92.0,
            }
        ],
    )
