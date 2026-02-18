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
- PostgreSQL
- Uvicorn
- Docker / Docker Compose

---

## 🚀 Ejecución

### 🐳 Opción A — Docker (recomendado)

La forma más simple de correr el proyecto. Solo necesitás tener **Docker Desktop** instalado y corriendo.

**1. Clonar el repositorio**

```bash
git clone https://github.com/Giuliano-Espejo/fastApi-Intento-1
cd fastApi-Intento-1
```

**2. Levantar los servicios**

```bash
docker-compose up -d --build
```

Esto levanta automáticamente:
- La base de datos PostgreSQL
- La API con hot-reload habilitado
- Crea las tablas si no existen

API disponible en: `http://localhost:8000`

**Comandos útiles**

```bash
docker-compose logs -f api       # Ver logs de la API en tiempo real
docker-compose logs -f db        # Ver logs de la base de datos
docker-compose down              # Detener los servicios
docker-compose down -v           # Detener y eliminar la base de datos
docker-compose up -d --build     # Reconstruir y levantar (tras cambios en dependencias)
```

> Con `--reload` activo, cualquier cambio en el código se aplica automáticamente sin necesidad de reiniciar.

---

### 💻 Opción B — Ejecución local

Requiere tener **PostgreSQL** instalado y corriendo localmente.

**1. Clonar el repositorio**

```bash
git clone https://github.com/Giuliano-Espejo/fastApi-Intento-1
cd fastApi-Intento-1
```

**2. Crear entorno virtual**

```bash
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows
```

**3. Instalar dependencias**

```bash
pip install -r requirements.txt
```

**4. Configurar la base de datos**

Asegurate de tener una base de datos PostgreSQL corriendo con los siguientes datos (o modificá `app/core/database.py`):

```
Usuario:   fastapi_user
Contraseña: secret
Base de datos: fastapi_app
Puerto: 5432
```

**5. Ejecutar la aplicación**

```bash
uvicorn main:app --reload --app-dir app
```

API disponible en: `http://localhost:8000`

---

## 📖 Documentación

Una vez corriendo el proyecto, la documentación interactiva está disponible en:

- **Swagger UI** → `http://localhost:8000/docs`
- **ReDoc** → `http://localhost:8000/redoc`

---

## 📦 Base de datos

- Base de datos: **PostgreSQL**
- Las tablas se crean automáticamente al iniciar la aplicación
- Al usar Docker, los datos persisten en un volumen (`postgres_data`)

⚠️ Si se modifican los modelos, por ahora no se usan migraciones. Para aplicar cambios:

```bash
docker-compose down -v   # Elimina el volumen con los datos
docker-compose up -d     # Vuelve a crear las tablas desde cero
```

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

### 📄 Listar pedidos

`GET /pedidos`

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

- **422 Unprocessable Entity** — Error de validación de entrada
- **404 Not Found** — Recurso inexistente
- **500 Internal Server Error** — Error no controlado

---

## 📈 Futuras mejoras

- Autenticación / autorización
- Migraciones con Alembic
- Soft delete

---

## 👨‍💻 Autor

Proyecto backend desarrollado con fines educativos y profesionales.