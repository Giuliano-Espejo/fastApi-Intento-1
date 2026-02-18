# Importa la clase principal de FastAPI.
# Esta clase representa la aplicación web.
from fastapi import FastAPI

# Importamos la función que crea las tablas
from core.database import create_db_and_tables

from routers import categoria, pedido, producto

# Crea la instancia de la aplicación.
# Acá FastAPI empieza a existir.
app = FastAPI(
    title="FoodStore FastApi",
    description="FoodStore en fastApi, gestor de pedidos para restaurantes",
    version="1.0.0"
)

# Registramos los routers
app.include_router(
    categoria.router
)

app.include_router(
    producto.router
)

app.include_router(
    pedido.router
)


# Evento que se ejecuta al iniciar la aplicación
@app.on_event("startup")
def on_startup():
    # Crea las tablas en la base de datos si no existen
    create_db_and_tables()

# Endpoint mínimo de prueba.
# Sirve solo para verificar que la app levanta.
@app.get("/")
def health_check():
    # Devuelve un JSON simple.
    # Si esto responde, la app está viva.
    return {"status":"ok"}