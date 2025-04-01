class CurrencyConverter:
    def __init__(self, csv_file="data/exchange_rates.csv"):
        self.rates = {}
        with open(csv_file, "r") as file:
            next(file)  # Пропускаем заголовок
            for line in file:
                currency, rate = line.strip().split(",")
                self.rates[currency] = float(rate)

    def convert(self, amount, from_currency, to_currency):
        if from_currency not in self.rates or to_currency not in self.rates:
            raise ValueError("Currency not found")
        return amount * (self.rates[to_currency] / self.rates[from_currency])
