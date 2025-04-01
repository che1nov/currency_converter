import csv
import json
from typing import Dict, List


class CurrencyConverter:
    def __init__(
        self,
        currencies_file: str = "currencies.csv",
        operations_file: str = "operations.json",
    ):
        """
        Инициализация конвертера.
        :param currencies_file: Путь к файлу с курсами валют.
        :param operations_file: Путь к файлу с историей операций.
        """
        self.currencies_file = currencies_file
        self.operations_file = operations_file
        self.rates = self.load_currencies()
        self.operations = self.load_operations()

    def load_currencies(self) -> Dict[str, float]:
        """
        Загрузка курсов валют из CSV-файла.
        :return: Словарь с курсами валют.
        """
        try:
            with open(self.currencies_file, mode="r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                return {row["currency"]: float(row["rate"]) for row in reader}
        except FileNotFoundError:
            print(f"Файл {self.currencies_file} не найден.")
            return {}

    def save_operations(self):
        """
        Сохранение истории операций в JSON-файл.
        """
        with open(self.operations_file, mode="w", encoding="utf-8") as file:
            json.dump(self.operations, file, indent=4)

    def load_operations(self) -> List[Dict]:
        """
        Загрузка истории операций из JSON-файла.
        :return: Список операций.
        """
        try:
            with open(self.operations_file, mode="r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Файл {self.operations_file} не найден.")
            return []

    def convert_currency(
        self, amount: float, from_currency: str, to_currency: str
    ) -> float:
        """
        Конвертация суммы из одной валюты в другую.
        :param amount: Сумма для конвертации.
        :param from_currency: Исходная валюта.
        :param to_currency: Целевая валюта.
        :return: Конвертированная сумма.
        """
        if from_currency not in self.rates or to_currency not in self.rates:
            raise ValueError(
                f"Курс для валюты {from_currency} или {to_currency} не найден."
            )
        rate_from = self.rates[from_currency]
        rate_to = self.rates[to_currency]
        converted_amount = (amount / rate_from) * rate_to
        self._log_operation(amount, from_currency, to_currency, converted_amount)
        return round(converted_amount, 2)

    def _log_operation(
        self, amount: float, from_currency: str, to_currency: str, result: float
    ):
        """
        Логирование операции в историю.
        :param amount: Сумма для конвертации.
        :param from_currency: Исходная валюта.
        :param to_currency: Целевая валюта.
        :param result: Результат конвертации.
        """
        operation = {
            "amount": amount,
            "from_currency": from_currency,
            "to_currency": to_currency,
            "result": result,
        }
        self.operations.append(operation)
        self.save_operations()

    def get_operations_history(self) -> List[Dict]:
        """
        Получение истории операций.
        :return: Список операций.
        """
        return self.operations
