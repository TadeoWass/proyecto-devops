# Stage 1: Build environment for dependencies
FROM python:3.8-slim AS build

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Stage 2: Production environment
FROM python:3.8-slim

WORKDIR /app

COPY --from=build /app .

CMD ["newrelic-admin", "run-program", "python", "app.py"]
