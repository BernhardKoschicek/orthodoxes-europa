# Multi-stage Containerfile for orthodoxes-europa
# Stage 1: Dependency builder using Astral uv
FROM python:3.13-slim-bookworm AS builder

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy

WORKDIR /app

COPY pyproject.toml uv.lock ./
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-install-project --no-dev

# Stage 2: Minimal unprivileged runner
FROM python:3.13-slim-bookworm AS runner

# Unprivileged user appuser with UID/GID 1000 matching Debian host user
RUN groupadd -g 1000 appuser && \
    useradd -u 1000 -g appuser -m -s /bin/bash appuser

WORKDIR /app

# Copy virtualenv from builder with matching path /app/.venv
COPY --from=builder --chown=appuser:appuser /app/.venv /app/.venv

# Copy application source and configuration
COPY --chown=appuser:appuser app /app/app
COPY --chown=appuser:appuser gunicorn.conf.py runserver.py pyproject.toml /app/

# Prepare storage directories and set permissions for UID 1000
RUN mkdir -p /storage/data /storage/media/thumbnails && \
    chown -R appuser:appuser /storage

ENV PATH="/app/.venv/bin:$PATH" \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    STORAGE_PATH=/storage \
    PORT=5000 \
    HOST=0.0.0.0

USER 1000:1000

EXPOSE 5000

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:5000/health')"

CMD ["gunicorn", "--config", "gunicorn.conf.py", "app:app"]
