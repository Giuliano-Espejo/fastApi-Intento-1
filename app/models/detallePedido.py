from typing import Optional
from sqlmodel import SQLModel, Field, Relationship

from .producto import Producto


class DetallePedido(SQLModel, table=True):
    """
    Entidad DetallePedido.

    UML:
    - No conoce a Pedido.
    - Pertenece conceptualmente a Pedido.
    - Conoce al Producto asociado.
    """

    # Identificador del detalle
    id: Optional[int] = Field(
        default=None,
        primary_key=True
    )

    # Cantidad de producto
    cantidad: int = Field(
        nullable=False,
        gt=0
    )


    # Relación con Producto
    # DetallePedido conoce al Producto
    producto_id: int = Field(
        foreign_key="producto.id",
        nullable=False
    )

    producto: Producto = Relationship()


    pedido_id: int = Field(foreign_key="pedido.id", nullable=False)


