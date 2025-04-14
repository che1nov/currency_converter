from app import CurrencyConverterHandler, run
from models import ExchangeRateLoader, CurrencyConverter
import unittest
from http.server import HTTPServer
from urllib.request import Request, urlopen
from urllib.error import HTTPError
import threading

class TestApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.loader = ExchangeRateLoader('exchange_rates.csv')
        cls.loader.load_rates()
        cls.converter = CurrencyConverter(cls.loader)
        cls.server = HTTPServer(('localhost', 8008), CurrencyConverterHandler)
        CurrencyConverterHandler.converter = cls.converter
        cls.server_thread = threading.Thread(target=cls.server.serve_forever)
        cls.server_thread.daemon = True
        cls.server_thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server_thread.join()

    def test_convert(self):
        url = 'http://localhost:8008/convert?amount=100&from=USD&to=EUR'
        response = urlopen(url)
        self.assertEqual(response.status, 200)
        data = eval(response.read().decode('utf-8'))
        self.assertEqual(data['amount'], 100)
        self.assertEqual(data['from'], 'USD')
        self.assertEqual(data['to'], 'EUR')
        self.assertAlmostEqual(data['result'], 85.0)

    def test_convert_missing_params(self):
        url = 'http://localhost:8008/convert?amount=100&from=USD'
        with self.assertRaises(HTTPError) as context:
            urlopen(url)
        self.assertEqual(context.exception.code, 400)

    def test_convert_invalid_currency(self):
        url = 'http://localhost:8008/convert?amount=100&from=USD&to=JPY'
        with self.assertRaises(HTTPError) as context:
            urlopen(url)
        self.assertEqual(context.exception.code, 400)

    def test_history(self):
        url = 'http://localhost:8008/history'
        response = urlopen(url)
        self.assertEqual(response.status, 200)
        data = eval(response.read().decode('utf-8'))
        self.assertEqual(data['history'], [])
