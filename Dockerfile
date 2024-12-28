FROM python:3.11-slim

# Install Poetry
RUN pip install --no-cache-dir poetry

WORKDIR /app

# Copy Poetry files
COPY pyproject.toml poetry.lock /app/

# Install dependencies using Poetry
RUN poetry config virtualenvs.create false && poetry install --no-dev --no-interaction --no-ansi

# Copy application code
COPY ./app /app

CMD ["python", "-m", "app"]
