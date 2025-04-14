# Dockerfile
FROM python:3.13-slim

# Установите рабочую директорию
WORKDIR /app

# Копируйте зависимости
COPY requirements.txt .

# Установите зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируйте исходный код
COPY . .

# Команда для запуска сервера
CMD ["python3", "app.py"]
