# Stage 1 
FROM python:3.11-alpine AS builder
WORKDIR /app
RUN apk add --no-cache build-base
COPY app/requirements.txt .
RUN pip install --upgrade pip && pip install --target=/install -r requirements.txt

# Stage 2 
FROM python:3.11-alpine
WORKDIR /app
RUN apk add --no-cache libffi openssl
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH 
COPY app/ .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]


