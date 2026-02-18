from typing import List, Optional
from models.rol import Rol
from sqlmodel import SQLModel, Field, Relationship


class Usuario(SQLModel, table=True):
    """
    Entidad Usuario.

    UML:
    - Usuario EXISTE por sí mismo
    - Pedido conoce a Usuario
    - Usuario NO conoce a Pedido (relación unidireccional)

    Por eso:
    - NO hay Relationship a Pedido
    - NO hay listas de pedidos acá
    """

    # Identificador único del usuario
    id: Optional[int] = Field(
        default=None,
        primary_key=True
    )

    # Nombre del usuario
    nombre: str = Field(
        min_length=3,
        max_length=50,
        nullable=False
    )

    apellido: str = Field(
        min_length=3,
        max_length=50,
        nullable=False
    )

    # Email del usuario
    # Es único porque identifica al usuario en el sistema
    mail: str = Field(
        index=True,
        nullable=False,
        max_length=100
    )

    # Rol del usuario dentro del sistema
    rol: Rol = Field(
        nullable=False
    )

    # Indica si el usuario está activo
    activo: bool = Field(
        default=True
    )

    celular: str = Field(
        min_length=9,
        max_length=9,
        nullable=False
    )

 # Relación con Pedido 
    pedidos: List["Pedido"] = Relationship()