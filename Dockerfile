FROM python:3.13-slim

RUN apt-get update && apt-get install -y \
    curl \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi --no-root --only main

COPY src/ ./src/

ENV PYTHONPATH=/app/src

EXPOSE 8000

CMD ["python", "src/hotel_booking/manage.py", "runserver", "0.0.0.0:8000"]
