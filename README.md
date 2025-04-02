# Currency Converter API

Этот API предоставляет инструменты для конвертации валют и получения списка всех операций.

### Конвертация валют
- URL: /convert
- Метод: POST
- Описание: Выполняет конвертацию суммы из одной валюты в другую.

Параметры запроса:

- amount (обязательный) — Сумма для конвертации.

- from_currency (обязательный) — Код исходной валюты (например, USD, EUR).

- to_currency (обязательный) — Код целевой валюты (например, JPY, GBP).

Пример запроса:
```
{
  "amount": 150,
  "from_currency": "USD",
  "to_currency": "EUR"
}

```
Пример ответа:

```
{
  "converted_amount": 138.75,
  "from_currency": "USD",
  "to_currency": "EUR",
  "rate": 0.925
}

```

### Получение всех операций

- URL: /operations
- Метод: GET
- Описание: Возвращает список всех выполненных операций конвертации.

Пример ответа:
````
[
  {
    "timestamp": "2025-04-02T23:46:00Z",
    "amount": 150,
    "from_currency": "USD",
    "to_currency": "EUR",
    "converted_amount": 138.75,
    "rate": 0.925
  },
  {
    "timestamp": "2025-04-02T22:15:00Z",
    "amount": 200,
    "from_currency": "EUR",
    "to_currency": "GBP",
    "converted_amount": 176.00,
    "rate": 0.88
  }
]
````
