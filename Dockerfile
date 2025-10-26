# syntax=docker/dockerfile:1
FROM python:3.12-slim

# Create a non-root user
RUN useradd -m appuser
WORKDIR /app

# Install system deps if needed (kept empty here)
RUN apt-get update && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Copy deps first for caching
COPY requirements.runtime.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy app
COPY . /app

USER appuser
EXPOSE 8000

# Run FastAPI with uvicorn
CMD ["uvicorn", "Main:api", "--host", "0.0.0.0", "--port", "8000"]
