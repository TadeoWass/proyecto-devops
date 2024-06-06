FROM python:3.8-slim

WORKDIR /app

COPY proyecto-devops/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY proyecto-devops/newrelic.ini /app/newrelic.ini
COPY proyecto-devops/app.py /app/app.py

CMD ["newrelic-admin", "run-program", "python", "/app/app.py"]
