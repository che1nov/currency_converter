from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from src.currency_converter import CurrencyConverter

converter = CurrencyConverter()


class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == "/convert":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data)
            try:
                result = converter.convert(data["amount"], data["from"], data["to"])
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"result": result}).encode())
            except ValueError as e:
                self.send_response(400)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"error": str(e)}).encode())

    def do_GET(self):
        if self.path == "/history":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"history": []}).encode())


def run(server_class=HTTPServer, handler_class=RequestHandler, port=8008):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
