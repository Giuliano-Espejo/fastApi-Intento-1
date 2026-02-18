from sqlmodel import Session, select

# Entity (modelo persistente)
from models.categoria import Categoria

# Schemas (DTOs)
from schemas.categoria import (
    CategoriaCreate,
    CategoriaEdit,
    CategoriaDto,
)

class CategoriaService:
    @staticmethod
    def crear_categoria(
        session: Session, categoria_create: CategoriaCreate
    ) -> CategoriaDto:
        """
        Crea una nueva categoría.

        Flujo:
        1. Recibe un DTO de entrada (CategoriaCreate)
        2. Crea la entidad Categoria
        3. Persiste en la base de datos
        4. Devuelve un DTO de salida (CategoriaDto)
        """

        # 1. Crear la entidad a partir del DTO
        categoria = Categoria(nombre=categoria_create.nombre)

        # 2. Guardar en base de datos
        session.add(categoria)
        session.commit()
        session.refresh(categoria)

        # 3. Mapear Entity → DTO
        return CategoriaDto(id=categoria.id, nombre=categoria.nombre)


    @staticmethod
    def listar_categorias(session: Session) -> list[CategoriaDto]:
        """
        Devuelve todas las categorías.

        No devuelve entidades.
        Devuelve DTOs.
        """

        statement = select(Categoria)
        categorias = session.exec(statement).all()

        return [
            CategoriaDto(id=categoria.id, nombre=categoria.nombre)
            for categoria in categorias
        ]


    @staticmethod
    def obtener_categoria_por_id(
        session: Session, categoria_id: int
    ) -> CategoriaDto | None:
        """
        Busca una categoría por ID.

        Si no existe:
        - Devuelve None
        - El router decide qué HTTP status usar
        """

        categoria = session.get(Categoria, categoria_id)

        if categoria is None:
            return None

        return CategoriaDto(id=categoria.id, nombre=categoria.nombre)


    @staticmethod
    def editar_categoria(
        session: Session, categoria_edit: CategoriaEdit
    ) -> CategoriaDto | None:
        """
        Edita una categoría existente.
        """

        categoria = session.get(Categoria, categoria_edit.id)

        if categoria is None:
            return None

        # Aplicar cambios
        categoria.nombre = categoria_edit.nombre

        session.add(categoria)
        session.commit()
        session.refresh(categoria)

        return CategoriaDto(id=categoria.id, nombre=categoria.nombre)


    @staticmethod
    def eliminar_categoria(session: Session, categoria_id: int) -> bool:
        """
        Elimina una categoría.

        Retorna:
        - True si se eliminó
        - False si no existía
        """

        categoria = session.get(Categoria, categoria_id)

        if categoria is None:
            return False

        session.delete(categoria)
        session.commit()

        return True
    

    @staticmethod
    def obtener_categoria_por_nombre(
        session: Session, nombreCategoria: str
    ) -> CategoriaDto | None:
        """
        Busca una categoría por ID.

        Si no existe:
        - Devuelve None
        - El router decide qué HTTP status usar
        """

        categoria = session.exec(
                select(Categoria).where(Categoria.nombre == nombreCategoria)
        ).first()

        

        if categoria is None:
            return None

        return CategoriaDto(id=categoria.id, nombre=categoria.nombre)