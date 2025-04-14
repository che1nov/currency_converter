from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class CurrencyConverterHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == "/convert":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length).decode("utf-8")
            try:
                data = json.loads(post_data)
                amount = data.get("amount")
                from_currency = data.get("from")
                to_currency = data.get("to")

                if not amount or not from_currency or not to_currency:
                    self.send_response(400)
                    self.end_headers()
                    self.wfile.write(b"Missing parameters")
                    return

                # Простая логика конвертации (замените на реальную)
                converted_amount = (
                    amount * 0.85
                    if from_currency == "USD" and to_currency == "EUR"
                    else None
                )
                if converted_amount is None:
                    self.send_response(400)
                    self.end_headers()
                    self.wfile.write(b"Invalid currency conversion")
                    return

                response = {
                    "amount": amount,
                    "from": from_currency,
                    "to": to_currency,
                    "result": converted_amount,
                }
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(response).encode("utf-8"))
            except json.JSONDecodeError:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b"Invalid JSON")
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not Found")

    def do_GET(self):
        if self.path == "/history":
            response = {"history": []}  # Пример пустой истории
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(response).encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not Found")


def run(server_class=HTTPServer, handler_class=CurrencyConverterHandler, port=8008):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
