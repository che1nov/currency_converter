from converter import CurrencyConverter


def main():
    # Создаем экземпляр конвертера
    converter = CurrencyConverter()

    # Пример конвертации валют
    try:
        amount = 100
        from_currency = "USD"
        to_currency = "EUR"
        result = converter.convert_currency(amount, from_currency, to_currency)
        print(f"{amount} {from_currency} = {result} {to_currency}")
    except ValueError as e:
        print(e)

    # Выводим историю операций
    operations = converter.get_operations_history()
    print("\nИстория операций:")
    for op in operations:
        print(op)


if __name__ == "__main__":
    main()
