
from datetime import date

# Session es la unidad de trabajo de SQLAlchemy / SQLModel.
# Representa una transacción contra la base de datos.
from sqlmodel import Session, select

# Entidades del dominio (persistentes)
from models.estadoPedido import EstadoPedido
from schemas.detalle_pedido import DetallePedidoDto
from models.pedido import Pedido
from models.producto import Producto
from models.detallePedido import DetallePedido

from schemas.pedido import PedidoCreate, PedidoDto

"""
Service de Pedido.

Este módulo contiene la lógica de negocio relacionada con pedidos.
NO contiene código HTTP.
NO conoce FastAPI.
NO devuelve responses.

Su única responsabilidad es:
- aplicar reglas del dominio
- construir entidades
- persistirlas correctamente
"""

class PedidoService:


    def crear_pedido(pedido_create: PedidoCreate, session: Session) -> PedidoDto:
        # 1. Crear el pedido (sin detalles todavía)
        pedido = Pedido(
            fecha=date.today(),
            estado=EstadoPedido.PENDIENTE,
            forma_pago=pedido_create.forma_pago,
            total=0
        )

        detalles: list[DetallePedido] = []

        # 2. Procesar cada detalle
        for detalle in pedido_create.detalles:

            # 2.1 Verificar que el producto exista
            producto = session.get(Producto, detalle.producto_id)
            if producto is None:
                raise ValueError(f"Producto {detalle.producto_id} no existe")

            # 2.2 Calcular subtotal
            subtotal = producto.precio * detalle.cantidad
            pedido.total += subtotal

            # 2.3 Crear detalle
            detalle_pedido = DetallePedido(
                producto_id=producto.id,
                cantidad=detalle.cantidad
            )

            detalles.append(detalle_pedido)

        # 3. Asociar detalles al pedido
        pedido.detalles = detalles

        # 4. Persistir
        session.add(pedido)
        session.commit()
        session.refresh(pedido)

        return pedido_to_dto(pedido)

    @staticmethod
    def listar_pedidos(session: Session) -> list[PedidoDto]:
        statement = select(Pedido)
        pedidos = session.exec(statement).all()

        return [pedido_to_dto(pedido) for pedido in pedidos]

    @staticmethod
    def obtener_pedido_por_id(
        session: Session, pedido_id: int
    ) -> PedidoDto | None:
        """
        Busca un pedido por ID.

        Si no existe:
        - Devuelve None
        - El router decide qué HTTP status usar
        """

        pedido = session.get(Pedido, pedido_id)

        if pedido is None:
            return None

        return pedido_to_dto(pedido)

   
def pedido_to_dto(pedido: Pedido) -> PedidoDto:
        """
        Mapea una entidad Pedido a PedidoDto.

        Regla:
        - El subtotal NO se guarda, se calcula.
        - El producto NO se expone, solo su id.
        """

        detalles_dto: list[DetallePedidoDto] = []

        for detalle in pedido.detalles:
            subtotal = detalle.cantidad * detalle.producto.precio

            detalles_dto.append(
                DetallePedidoDto(
                    id=detalle.id,
                    producto_id=detalle.producto_id,
                    cantidad=detalle.cantidad,
                    subtotal=subtotal
                )
            )

        return PedidoDto(
            id=pedido.id,
            fecha=pedido.fecha,
            estado=pedido.estado,
            total=pedido.total,
            detalles=detalles_dto
        )