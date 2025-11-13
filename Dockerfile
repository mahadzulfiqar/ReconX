# ---------------------------------------------------------------------
# ReconX — Modular Reconnaissance Toolkit
# Dockerfile for containerized execution
# ---------------------------------------------------------------------

# Use official Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy dependency list first (for better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy entire project into container
COPY . /app

# Set default command
ENTRYPOINT ["python", "main.py"]

# Example usage:
# docker build -t reconx .
# docker run --rm reconx --target example.com --mode passive --output reports/out.json
