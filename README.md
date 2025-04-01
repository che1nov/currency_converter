## Currency Converter

## Project Description
Currency Converter is a simple Python web application that allows you to convert an amount from one currency to another and save the history of operations. The application uses an HTTP server to handle requests and supports loading currency rates from a CSV file.

## Main Features:
- **Currency Conversion**: User can send POST request with amount, source and target currency to get converted amount.
- **Transaction History**: All conversions performed are saved to a JSON file and can be accessed via a GET request.
- **Loading Currency Rates**: Exchange rates are loaded from a CSV file or can be customised via .env.

## Testing
To run tests use:
```bash
pytest tests/
```

## Configuration
- **.env**: Used to configure currency rates and other parameters.
- **currencies.csv**: File with currency rates.

## Project structure
- `server.py`: Main server file.
- `tests/`: Directory with tests.
- `operations.json`: File for storing the history of operations.
- `index.html`, `script.js`, `style.css`: Files for the frontend.

## Licence
This project is licensed under the MIT Licence.

Translated with DeepL.com (free version)
