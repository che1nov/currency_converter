from currency_converter import CurrencyConverter
from history_manager import HistoryManager


def main():
    # Инициализация конвертера валют
    converter = CurrencyConverter("exchange_rates.csv")

    # Инициализация менеджера истории операций
    history_manager = HistoryManager()

    # Примеры операций
    try:
        # Конвертация 100 USD в EUR
        amount = 100
        from_currency = "USD"
        to_currency = "EUR"
        converted_amount = converter.convert(amount, from_currency, to_currency)
        print(f"{amount} {from_currency} = {converted_amount} {to_currency}")

        # Добавление операции в историю
        operation = {
            "amount": amount,
            "from_currency": from_currency,
            "to_currency": to_currency,
            "converted_amount": converted_amount,
        }
        history_manager.add_operation(operation)

        # Конвертация 50 EUR в GBP
        amount = 50
        from_currency = "EUR"
        to_currency = "GBP"
        converted_amount = converter.convert(amount, from_currency, to_currency)
        print(f"{amount} {from_currency} = {converted_amount} {to_currency}")

        # Добавление операции в историю
        operation = {
            "amount": amount,
            "from_currency": from_currency,
            "to_currency": to_currency,
            "converted_amount": converted_amount,
        }
        history_manager.add_operation(operation)

        # Вывод истории операций
        print("\nИстория операций:")
        for op in history_manager.get_operations():
            print(op)

    except ValueError as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
