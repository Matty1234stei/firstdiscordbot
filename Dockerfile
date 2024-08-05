# Use the official Python image from the Docker Hub
FROM python:3.12-slim

# Set environment variables to avoid prompt during Poetry installation
ENV POETRY_VERSION=1.8.2
ENV POETRY_NO_INTERACTION=1
ENV POETRY_VIRTUALENVS_CREATE=false

# Install Poetry
RUN pip install "poetry==$POETRY_VERSION"

# Set the working directory inside the container
WORKDIR /app

# Copy only the necessary files for installing dependencies
COPY pyproject.toml poetry.lock ./

# Install dependencies using Poetry
RUN poetry install --no-root

# Copy the rest of the application code
COPY . .

# Command to run the application
CMD ["python", "src/main.py"]
