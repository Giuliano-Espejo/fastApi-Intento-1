# 🧾 API de Gestión de Pedidos

API REST desarrollada con **FastAPI** para la gestión de pedidos, productos y detalles de pedido.
El proyecto sigue una **arquitectura por capas**, separando responsabilidades entre rutas, servicios, modelos y DTOs.

Este backend está pensado como base sólida, clara y extensible, priorizando legibilidad, separación de responsabilidades y buenas prácticas.

### Capas

**routers**
- Definen endpoints HTTP
- No contienen lógica de negocio
- Solo validan entrada/salida

**services**
- Contienen la lógica de negocio
- Manejan transacciones
- Orquestan relaciones entre entidades

**models**
- Entidades persistidas en la base de datos
- Definen relaciones y columnas

**schemas (DTOs)**
- Modelos de entrada y salida
- Aíslan la API del ORM

---

## 🛠️ Tecnologías

- Python 3.11+
- FastAPI
- SQLModel
- SQLAlchemy
- SQLite
- Uvicorn

---

## 🚀 Instalación y ejecución

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/Giuliano-Espejo/fastApi-Intento-1
cd fastApi-Intento-1
```

### 2️⃣ Crear entorno virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows
```

### 3️⃣ Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4️⃣ Ejecutar la aplicación

```bash
uvicorn app.main:app --reload
```

API disponible en:
```
http://localhost:8000
```

Documentación automática:
- Swagger UI → `/docs`
- ReDoc → `/redoc`

---

## 📦 Base de datos

- Base de datos: **SQLite**
- Se inicializa automáticamente al iniciar la app
- Ideal para desarrollo

⚠️ Si se modifican los modelos:
- Eliminar el archivo `.db`
- Reiniciar la aplicación

(No se usan migraciones en esta etapa)

---

## 📌 Endpoints principales

### ➕ Crear pedido

`POST /pedidos`

```json
{
  "usuario_id": 1,
  "forma_pago": "EFECTIVO",
  "detalles": [
    {
      "producto_id": 1,
      "cantidad": 2
    }
  ]
}
```

---

### 📄 Listar pedidos

`GET /pedidos`

Respuesta:

```json
[
  {
    "id": 1,
    "fecha": "2026-02-18",
    "total": 2500.0,
    "forma_pago": "EFECTIVO",
    "estado": "CREADO",
    "detalles": [
      {
        "producto": "Teclado",
        "cantidad": 2,
        "precio_unitario": 1250.0
      }
    ]
  }
]
```

---

## ⚠️ Decisiones de diseño

- ❌ No se devuelven entidades 
- ✅ Uso estricto de DTOs
- ❌ No hay lógica en los routers
- ✅ Servicios como núcleo del sistema
- ✅ Relaciones manejadas explícitamente

---

## 🧪 Manejo de errores

- **422 Unprocessable Entity**
  Error de validación de entrada

- **404 Not Found**
  Recurso inexistente

- **500 Internal Server Error**
  Error no controlado

---

## 📈 Futuras mejoras

- Autenticación / autorización
- PostgreSQL
- Soft delete

---

## 👨‍💻 Autor

Proyecto backend desarrollado con fines educativos y profesionales.
