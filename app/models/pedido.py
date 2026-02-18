from typing import Optional, List
from models.usuario import Usuario
from models.estadoPedido import EstadoPedido
from models.metodoPago import MetodoPago
from sqlmodel import SQLModel, Field, Relationship
from models.detallePedido import DetallePedido

class Pedido(SQLModel, table=True):
    """
    Entidad Pedido (Agregado raíz).

    UML:
    - Pedido conoce a DetallePedido.
    - Es dueño del ciclo de vida de los detalles.
    - Los detalles no existen fuera del pedido.
    """

    # Identificador del pedido
    id: Optional[int] = Field(
        default=None,
        primary_key=True
    )

    # Fecha del pedido
    fecha: str = Field(
        nullable=False
    )

    # Total del pedido
    total: float = Field(
        nullable=False,
        ge=0
    )

    forma_pago: MetodoPago = Field(
        nullable=False
    )

    estado: EstadoPedido = EstadoPedido.PENDIENTE

    # Relación 1..N con DetallePedido
    # Pedido puede navegar hacia sus detalles
    detalles: List[DetallePedido] = Relationship(
        
         sa_relationship_kwargs={
            "cascade": "all, delete-orphan"
        }
    )

    usuario_id: int = Field(foreign_key="usuario.id")

    usuario: Optional["Usuario"] = Relationship(back_populates="pedidos")
