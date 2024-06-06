FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Copiar el archivo newrelic.ini
COPY newrelic.ini /app/newrelic.ini

# Establecer la variable de entorno para New Relic
ENV NEW_RELIC_CONFIG_FILE=/app/newrelic.ini

CMD ["newrelic-admin", "run-program", "python", "app.py"]
