from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from models import ExchangeRateLoader, CurrencyConverter
import json

class CurrencyConverterHandler(BaseHTTPRequestHandler):
    history = []  # Лог для хранения истории операций

    def do_POST(self):
        parsed_url = urlparse(self.path)
        path = parsed_url.path

        if path == '/convert':
            # Читаем данные из тела запроса
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            try:
                # Преобразуем JSON-данные в словарь
                data = json.loads(post_data)
                amount = data.get('amount')
                from_currency = data.get('from')
                to_currency = data.get('to')

                if not amount or not from_currency or not to_currency:
                    self.send_response(400)
                    self.end_headers()
                    self.wfile.write(b"Missing parameters")
                    return

                try:
                    amount = float(amount)
                    converted_amount = self.converter.convert(amount, from_currency, to_currency)

                    # Сохраняем операцию в историю
                    operation = {
                        "amount": amount,
                        "from": from_currency,
                        "to": to_currency,
                        "result": converted_amount
                    }
                    self.__class__.history.append(operation)

                    response = {
                        "amount": amount,
                        "from": from_currency,
                        "to": to_currency,
                        "result": converted_amount
                    }
                    self.send_response(200)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps(response).encode('utf-8'))
                except ValueError as e:
                    self.send_response(400)
                    self.end_headers()
                    self.wfile.write(json.dumps({"error": str(e)}).encode('utf-8'))
            except json.JSONDecodeError:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b"Invalid JSON")
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not Found")

    def do_GET(self):
        parsed_url = urlparse(self.path)
        path = parsed_url.path

        if path == '/history':
            # Возвращаем историю операций
            response = {"history": self.__class__.history}
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not Found")


def run(server_class=HTTPServer, handler_class=CurrencyConverterHandler, port=8008):
    loader = ExchangeRateLoader('exchange_rates.csv')
    loader.load_rates()
    converter = CurrencyConverter(loader)
    handler_class.converter = converter

    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd server on port {port}')
    httpd.serve_forever()


if __name__ == '__main__':
    run()
