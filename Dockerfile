# Multi-stage build untuk optimasi ukuran image
FROM python:3.10-slim as builder

# Set working directory
WORKDIR /app

# Copy requirements dan install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# Stage kedua untuk runtime
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy installed packages dari stage builder
COPY --from=builder /root/.local /root/.local

# Copy source code
COPY app.py .

# Make sure scripts in .local are usable
ENV PATH=/root/.local/bin:$PATH

# Expose port (opsional untuk demo)
EXPOSE 8080

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD python -c "import app; print('Health check passed')" || exit 1

# User non-root untuk security
RUN adduser --disabled-password --gecos '' appuser
USER appuser

# Command untuk menjalankan aplikasi
CMD ["python", "app.py"]
