# Currency Converter API

This project provides a RESTful API for currency conversion.

### Endpoints

### 1. Currency Conversion
- **URL**: `/convert`.
- **Method**: `POST`.

**Query Body**:
```json
{
    "amount": 100,
    "from": "USD",
    "to": "EUR"
}
```
**Expected response:**
```json
{
  "amount": 100.0,
  "from": "USD",
  "to": "EUR",
  "result": 85.0
}
```

### 2. Retrieving transaction history

- **URL:** `/history`.
- **Method**: `GET`.

**Expected Response**:
```json
{
  "history": [
    {
      "amount": 100.0,
      "from": "USD",
      "to": "EUR",
      "result": 85.0
    }
  ]
}
```
