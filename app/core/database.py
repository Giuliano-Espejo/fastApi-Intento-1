# SQLModel es el ORM que combina SQLAlchemy + Pydantic
from sqlmodel import SQLModel, create_engine, Session

# URL de conexión a la base de datos.
# SQLite guarda todo en un archivo local.
DATABASE_URL = "sqlite:///./prog3.db"



# Engine = objeto central que maneja la conexión con la DB.
# echo=True hace que se muestren las queries por consola (solo dev).
engine = create_engine(
    DATABASE_URL,
    echo=True
)


# Función utilitaria para crear todas las tablas.
# Lee todos los modelos que hereden de SQLModel con table=True.
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


# Dependency para obtener una sesión de base de datos.
# Se usa en repositorios y servicios.
def get_session():
    with Session(engine) as session:
        yield session