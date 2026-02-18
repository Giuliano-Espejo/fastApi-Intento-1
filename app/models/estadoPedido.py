from enum import Enum

class EstadoPedido(str, Enum):
    PENDIENTE = "PENDIENTE"
    PAGADO = "PAGADO"
    EN_PREPARACION = "EN_PREPARACION"
    ENVIADO = "ENVIADO"
    CANCELADO = "CANCELADO"
