FROM python:3.11-slim

WORKDIR /app/library

RUN apt-get update && apt-get install -y \
    libpq-dev gcc build-essential --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/library/

RUN pip install --no-cache-dir -r /app/library/requirements.txt

COPY . /app

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


