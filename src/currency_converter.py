import csv
import io


class CurrencyConverter:
    def __init__(self, csv_file="data/exchange_rates.csv"):
        self.rates = {}
        self.load_rates(csv_file)

    def load_rates(self, csv_file):
        """
        Load exchange rates from a CSV file or file-like object.
        Supports both file paths and StringIO objects.
        """
        if isinstance(csv_file, str):  # If it's a file path
            with open(csv_file, mode="r", newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.rates[row["currency"]] = float(row["rate"])
        elif isinstance(csv_file, io.TextIOBase):  # If it's a file-like object
            reader = csv.DictReader(csv_file)
            for row in reader:
                self.rates[row["currency"]] = float(row["rate"])
        else:
            raise ValueError("csv_file must be a file path or a file-like object")

    def convert(self, amount, from_currency, to_currency):
        """
        Convert an amount from one currency to another.
        """
        if from_currency not in self.rates or to_currency not in self.rates:
            raise ValueError(f"Invalid currency: {from_currency} or {to_currency}")
        return amount * (self.rates[to_currency] / self.rates[from_currency])
