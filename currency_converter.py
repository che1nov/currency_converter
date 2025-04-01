import csv


class CurrencyConverter:
    def __init__(self, csv_file):
        """
        Инициализация конвертера с курсами валют из CSV-файла.
        :param csv_file: Путь к CSV-файлу с курсами валют.
        """
        self.rates = self._load_rates_from_csv(csv_file)

    def _load_rates_from_csv(self, csv_file):
        """
        Загрузка курсов валют из CSV-файла.
        :param csv_file: Путь к CSV-файлу.
        :return: Словарь с курсами валют.
        """
        rates = {}
        with open(csv_file, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                currency = row["Currency"]
                rate = float(row["Rate"])
                rates[currency] = rate
        return rates

    def convert(self, amount, from_currency, to_currency):
        """
        Конвертация суммы из одной валюты в другую.
        :param amount: Сумма для конвертации.
        :param from_currency: Исходная валюта.
        :param to_currency: Целевая валюта.
        :return: Сконвертированная сумма.
        """
        if from_currency not in self.rates or to_currency not in self.rates:
            raise ValueError("Валюта не поддерживается.")

        # Переводим сумму в базовую валюту (например, USD)
        base_amount = amount / self.rates[from_currency]
        # Переводим из базовой валюты в целевую
        converted_amount = base_amount * self.rates[to_currency]
        return round(converted_amount, 2)
