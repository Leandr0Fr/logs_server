FROM python:3.12-slim

WORKDIR /src

# Install system dependencies required for building python packages (e.g. asyncpg)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY src/ ./src/
COPY .env .

# Create logs directory
RUN mkdir -p logs

# Expose port
EXPOSE 8080

# Run commands
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8080"]
