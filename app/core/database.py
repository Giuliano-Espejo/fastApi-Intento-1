import os
from sqlmodel import SQLModel, create_engine, Session

# Lee la URL del entorno, con fallback para desarrollo local
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg://fastapi_user:secret@localhost:5432/fastapi_app"
)

engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session