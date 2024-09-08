# Stage 1: Build stage
FROM python:3.12.5-slim-bookworm AS builder
LABEL maintainer="Justin Largo <justinlargo7@gmail.com>"
# Set environment variables
ENV POETRY_VERSION=1.8.3
ENV POETRY_VIRTUALENVS_CREATE=false
ENV POETRY_NO_INTERACTION=1

# Install Poetry
RUN pip install "poetry==$POETRY_VERSION"

# Set the working directory in the container
WORKDIR /app

# Copy the pyproject.toml and poetry.lock files
COPY pyproject.toml poetry.lock ./

# Install the dependencies
RUN poetry install --no-dev --no-root

# Copy the current directory contents into the container at /app
COPY . .

# Expose port 8000 for FastAPI
EXPOSE 8000

# Command to run the application
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

# Todo: make this a multi stage build