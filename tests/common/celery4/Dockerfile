FROM python:3.9-slim-buster

# Create a user to run the worker
RUN adduser --disabled-password --gecos "" test_user

# Install system dependencies
RUN apt-get update && apt-get install -y build-essential

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir celery[redis]==4.4.7

# Copy the rest of the app
WORKDIR /app

# Switch to the test_user
USER test_user

# Start the celery worker
CMD celery -A app worker --loglevel=info -n celery4_test_worker@%h