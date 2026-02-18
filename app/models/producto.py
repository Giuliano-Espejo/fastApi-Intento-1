from typing import Optional
from sqlmodel import SQLModel, Field, Relationship

from models.categoria import Categoria


class Producto(SQLModel, table=True):
    """
    Entidad Producto.

    Según el UML:
    - Producto pertenece a una Categoria.
    - La relación es unidireccional:
        Producto → Categoria
    - Categoria no sabe nada de Producto.
    """

    # Clave primaria
    id: Optional[int] = Field(
        default=None,
        primary_key=True
    )

    # Nombre del producto
    nombre: str = Field(
        nullable=False,
        max_length=100
    )

    # Precio del producto
    # gt=0 asegura que no se guarden precios inválidos
    precio: float = Field(
        nullable=False,
        gt=0
    )

    # Stock disponible
    stock: int = Field(
        nullable=False,
        ge=0
    )

    # ---------- RELACIÓN CON CATEGORIA ----------

    # Foreign Key REAL en la base de datos
    # Esta columna materializa la relación del UML
    categoria_id: int = Field(
        foreign_key="categoria.id",
        nullable=False
    )

    # Relación ORM unidireccional
    # Permite hacer: producto.categoria
    # NO existe categoria.productos
    categoria: Categoria = Relationship()
