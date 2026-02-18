FROM python:3.11-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Evita que Python genere archivos .pyc y fuerza logs sin buffer
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Dependencias del sistema necesarias para psycopg2
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Instalar dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copiar el código de la aplicación
COPY . .

# Puerto que expone la API
EXPOSE 8000

# En desarrollo el comando lo sobreescribe docker-compose,
# pero dejamos uno por defecto igual
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
