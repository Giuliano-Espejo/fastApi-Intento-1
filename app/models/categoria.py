from typing import Optional
from sqlmodel import SQLModel, Field


class Categoria(SQLModel, table=True):
    """
    Entidad Categoria.

    Según el UML:
    - Categoria es un concepto independiente.
    - NO navega hacia Producto.
    - NO conoce qué productos existen.
    - Solo define información propia.
    """

    # Clave primaria
    # Optional porque:
    # - al crear el objeto aún no existe
    # - la base de datos lo genera
    id: Optional[int] = Field(
        default=None,
        primary_key=True
    )

    # Nombre de la categoría
    # Es obligatorio: una categoría sin nombre no tiene sentido
    nombre: str = Field(
        nullable=False,
        index=True,
        max_length=50
    )
