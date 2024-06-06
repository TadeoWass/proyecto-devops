FROM python:3.8-slim

WORKDIR /app

COPY proyecto-devops/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY proyecto-devops/newrelic.ini /app/newrelic.ini
COPY proyecto-devops/. .

CMD ["newrelic-admin", "run-program", "python", "proyecto-devops/app.py"]
