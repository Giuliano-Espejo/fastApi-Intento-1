from sqlmodel import Session, select

# Entity (modelo persistente)
from models.categoria import Categoria
from models.producto import Producto

# Schemas (DTOs)
from schemas.producto import (
    ProductoCreate,
    ProductoEdit,
    ProductoDto,
)


class ProductoService:
    @staticmethod
    def crear_producto(
        session: Session, producto_create: ProductoCreate
    ) -> ProductoCreate:
        """
        Crea una nuevo producto.

        Flujo:
        1. Recibe un DTO de entrada (ProductoCreate)
        2. Crea la entidad Producto
        3. Persiste en la base de datos
        4. Devuelve un DTO de salida (ProductoDto)
        """

        # 1. Buscar la categoría asociada
        categoria_buscada = session.get(Categoria, producto_create.categoria_id)

        if categoria_buscada is None:
            raise ValueError("La categoría indicada no existe")

        # 2. Crear la entidad a partir del DTO
        producto = Producto(
            nombre=producto_create.nombre,
            precio=producto_create.precio,
            stock=producto_create.stock,
            categoria=categoria_buscada,
        )

        # 3. Guardar en base de datos
        session.add(producto)
        session.commit()
        session.refresh(producto)

        # 4. Mapear Entity → DTO
        return ProductoDto(
            id=producto.id,
            nombre=producto.nombre,
            precio=producto.precio,
            stock=producto.stock,
            categoria_id=producto.categoria.id,
        )

    @staticmethod
    def listar_productos(session: Session) -> list[ProductoDto]:
        """
        Devuelve todas los productos.

        No devuelve entidades.
         Devuelve DTOs.
        """

        statement = select(Producto)
        productos = session.exec(statement).all()

        return [
            ProductoDto(
                id=producto.id,
                nombre=producto.nombre,
                precio=producto.precio,
                stock=producto.stock,
                categoria_id=producto.categoria.id,
            )
            for producto in productos
        ]

    @staticmethod
    def obtener_producto_por_id(
        session: Session, producto_id: int
    ) -> ProductoDto | None:
        """
        Busca un producto por ID.
        Si no existe:
        - Devuelve None
        - El router decide qué HTTP status usar
        """

        producto = session.get(Producto, producto_id)

        if producto is None:
            return None

        return ProductoDto(
            id=producto.id,
            nombre=producto.nombre,
            precio=producto.precio,
            stock=producto.stock,
            categoria_id=producto.categoria.id,
        )

    @staticmethod
    def editar_producto(
        session: Session, producto_edit: ProductoEdit
    ) -> ProductoDto | None:
        """
        Edita una producto existente.
        """

        producto = session.get(Producto, producto_edit.id)

        if producto is None:
            return None

        # Aplicar cambios
        producto.nombre = producto_edit.nombre
        producto.precio = producto_edit.precio
        producto.stock = producto_edit.stock

        session.add(producto)
        session.commit()
        session.refresh(producto)

        return ProductoDto(
            id=producto.id,
            nombre=producto.nombre,
            precio=producto.precio,
            stock=producto.stock,
            categoria_id=producto.categoria.id,
        )

    @staticmethod
    def eliminar_producto(session: Session, producto_id: int) -> bool:
        """
        Elimina un producto.

        Retorna:
        - True si se eliminó
        - False si no existía
        """

        producto = session.get(Producto, producto_id)

        if producto is None:
            return False

        session.delete(producto)
        session.commit()

        return True

   