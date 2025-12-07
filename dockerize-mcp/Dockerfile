# syntax=docker/dockerfile:1
FROM python:3.12-slim-bullseye AS base

RUN apt-get update && rm -rf /var/lib/apt/lists/*

# Install uv package manager
RUN pip install --no-cache-dir uv

WORKDIR /app

# Copy dependency files
COPY pyproject.toml uv.lock ./

# Install dependencies using uv (fast resolver)
RUN uv sync --frozen --no-cache

# Copy project code
COPY . .

# Expose port for MCP
EXPOSE 8000

# Start MCP server
CMD ["uv", "run", "main.py"]