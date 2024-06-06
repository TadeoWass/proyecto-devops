FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY newrelic.ini /app/newrelic.ini
COPY app.py /app/app.py

CMD ["newrelic-admin", "run-program", "python", "/app/app.py"]
