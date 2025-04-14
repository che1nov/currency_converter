from models import ExchangeRateLoader, CurrencyConverter

def main():
    loader = ExchangeRateLoader('exchange_rates.csv')
    loader.load_rates()
    converter = CurrencyConverter(loader)

    # Пример использования
    try:
        amount = 100
        from_currency = 'USD'
        to_currency = 'EUR'
        converted_amount = converter.convert(amount, from_currency, to_currency)
        print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
