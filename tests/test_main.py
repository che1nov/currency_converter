from unittest.mock import patch
from main import main


def test_main(capsys):
    with patch("builtins.print") as mock_print:
        main()

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
