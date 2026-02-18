from pydantic import BaseModel

class DetallePedidoCreate(BaseModel):
    """
    Equivalente a DetallePedidoCreate.java

    Se usa al crear un pedido.
    """

    producto_id: int
    cantidad: int

class DetallePedidoDto(BaseModel):
    """
    Equivalente a DetallePedidoDto.java

    DTO de salida.
    """

    id: int
    producto_id: int
    cantidad: int
    subtotal: float
