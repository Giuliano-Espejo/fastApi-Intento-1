from fastapi import APIRouter, Depends,  status
from sqlmodel import Session
from core.database import get_session
from schemas.pedido import PedidoCreate, PedidoDto
from services.pedido_service import PedidoService

router = APIRouter(
    prefix="/pedidos",
    tags=["Pedidos"]
)

@router.post("/", response_model=PedidoDto,          
    status_code=status.HTTP_201_CREATED )
def crear_pedido(pedido: PedidoCreate, session: Session=Depends(get_session)):
    """
    Endpoint para crear un pedido.

    En este paso:
    - Solo recibe y valida datos
    - NO guarda en base de datos
    - NO calcula totales
    """

    return PedidoService.crear_pedido(pedido,session)


@router.get("/", response_model=list[PedidoDto])
def listar_pedidos(session: Session = Depends(get_session)):
    """
    Lista todos los pedidos.

    En este paso:
    - No hay paginado
    - No hay filtros
    """

    return PedidoService.listar_pedidos(session)
