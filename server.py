import os
import csv
import json
import http.server
import socketserver
from dotenv import load_dotenv


# Загрузка переменных окружения из .env-файла
load_dotenv()

# Параметры приложения
CURRENCIES_FILE = os.getenv("CURRENCIES_FILE", "currencies.csv")
OPERATIONS_FILE = os.getenv("OPERATIONS_FILE", "operations.json")


# Загрузка курсов валют из CSV-файла
def load_currencies(file_path=CURRENCIES_FILE):
    if not os.path.exists(file_path):
        return {}
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return {row['currency']: float(row['rate']) for row in reader}


# Сохранение операций в JSON-файл
def save_operations(operations, file_path=OPERATIONS_FILE):
    with open(file_path, mode='w', encoding='utf-8') as file:
        json.dump(operations, file, indent=4)


# Загрузка операций из JSON-файла
def load_operations(file_path=OPERATIONS_FILE):
    if not os.path.exists(file_path):
        return []
    with open(file_path, mode='r', encoding='utf-8') as file:
        return json.load(file)


# Конвертация суммы из одной валюты в другую
def convert_currency(amount, from_currency, to_currency, rates):
    if from_currency not in rates or to_currency not in rates:
        return None
    rate_from = rates[from_currency]
    rate_to = rates[to_currency]
    converted_amount = (amount / rate_from) * rate_to
    return round(converted_amount, 2)


# Обработчик запросов
class CurrencyConverterHandler(http.server.BaseHTTPRequestHandler):

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_GET(self):
        if self.path == "/operations":
            operations = load_operations()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps(operations).encode("utf-8"))
        else:
            self.send_error(404, "Not Found")

    def do_POST(self):
        if self.path == "/convert":
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length).decode("utf-8")
            try:
                data = json.loads(body)
                amount = float(data.get("amount", 0))
                from_currency = data.get("from_currency", "").upper()
                to_currency = data.get("to_currency", "").upper()

                rates = load_currencies()
                result = convert_currency(amount, from_currency, to_currency, rates)

                if result is None:
                    self.send_error(400, "Invalid currency")
                    return

                # Сохраняем операцию в историю
                operations = load_operations()
                operations.append({
                    "amount": amount,
                    "from_currency": from_currency,
                    "to_currency": to_currency,
                    "result": result
                })
                save_operations(operations)

                # Отправляем ответ
                response = {
                    "converted_amount": result,
                    "from_currency": from_currency,
                    "to_currency": to_currency
                }
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                self.wfile.write(json.dumps(response).encode("utf-8"))

            except (ValueError, KeyError):
                self.send_error(400, "Invalid request body")
        else:
            self.send_error(404, "Not Found")


# Функция для получения порта
def get_port():
    return int(os.getenv("SERVER_PORT", 8000))


# Запуск сервера
if __name__ == "__main__":
    PORT = get_port()
    with socketserver.TCPServer(("", PORT), CurrencyConverterHandler) as httpd:
        print(f"Serving on port {PORT}...")
        httpd.serve_forever()
