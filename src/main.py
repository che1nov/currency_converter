from unittest.mock import patch
from main import main


def test_main(capsys, tmp_path):
    # Создаем временный CSV-файл с курсами валют
    csv_content = "Currency,Rate\nUSD,1.0\nEUR,0.92\nGBP,0.79\nRUB,76.5"
    csv_file = tmp_path / "test_rates.csv"
    csv_file.write_text(csv_content)

    # Мокируем путь к CSV-файлу
    with patch("src.currency_converter.CurrencyConverter.__init__") as mock_init:
        mock_init.return_value = None  # Отключаем реальный конструктор
        with patch("builtins.print") as mock_print:
            main()

    # Проверяем вывод на экран
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
