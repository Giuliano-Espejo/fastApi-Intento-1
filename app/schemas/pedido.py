from datetime import date
from typing import List
from pydantic import BaseModel
from models.estadoPedido import EstadoPedido
from models.metodoPago import MetodoPago

from .detalle_pedido import DetallePedidoCreate, DetallePedidoDto

class PedidoCreate(BaseModel):
    """
    Equivalente a PedidoCreate.java

    Se usa para crear pedidos.
    """

    forma_pago: MetodoPago
    detalles: List[DetallePedidoCreate]


class PedidoDto(BaseModel):
    """
    Equivalente a PedidoDto.java

    DTO de salida del pedido completo.
    """

    id: int
    fecha: date
    estado: EstadoPedido
    total: float
    detalles: List[DetallePedidoDto]

