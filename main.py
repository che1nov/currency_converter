from currency_converter import CurrencyConverter
from history_manager import HistoryManager


def main():
    converter = CurrencyConverter("exchange_rates.csv")
    history_manager = HistoryManager()

    # Пример операции
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
    print("History:", history_manager.get_operations())


if __name__ == "__main__":
    main()
