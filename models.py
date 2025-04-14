import csv
from typing import Dict

class ExchangeRateLoader:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.rates = {}

    def load_rates(self):
        with open(self.file_path, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.rates[row['currency']] = float(row['rate'])

    def get_rate(self, currency: str) -> float:
        return self.rates.get(currency, None)

class CurrencyConverter:
    def __init__(self, loader: ExchangeRateLoader):
        self.loader = loader

    def convert(self, amount: float, from_currency: str, to_currency: str) -> float:
        from_rate = self.loader.get_rate(from_currency)
        to_rate = self.loader.get_rate(to_currency)
        if from_rate is None or to_rate is None:
            raise ValueError("Invalid currency")
        return (amount / from_rate) * to_rate
