


# Session es la unidad de trabajo de SQLAlchemy / SQLModel.
# Representa una transacción contra la base de datos.
from sqlmodel import Session, select

from models.rol import Rol
from models.usuario import Usuario

from schemas.usuario import UsuarioCreate, UsuarioDto, UsuarioEdit

"""
Service de Usuario.

Este módulo contiene la lógica de negocio relacionada con usuario.
NO contiene código HTTP.
NO conoce FastAPI.
NO devuelve responses.

Su única responsabilidad es:
- aplicar reglas del dominio
- construir entidades
- persistirlas correctamente
"""

class UsuarioService:

    @staticmethod
    def crear_usuario(
        session: Session, usuairo_create: UsuarioCreate
    ) -> UsuarioDto:
        """
        Crea una nuevo usuario.

        Flujo:
        1. Recibe un DTO de entrada (Usuarioreate)
        2. Crea la entidad Usuario
        3. Persiste en la base de datos
        4. Devuelve un DTO de salida (UsuarioDto)
        """

        # 1. Crear la entidad a partir del DTO
        usuario = Usuario (
            nombre=usuairo_create.nombre,
            apellido=usuairo_create.apellido,
            mail=usuairo_create.mail,
            rol=Rol.USUARIO,
            celular=usuairo_create.celular,
            contrasena=usuairo_create.contrasena,
            pedidos=[]
        )

        # 3. Guardar en base de datos
        session.add(usuario)
        session.commit()
        session.refresh(usuario)

        # 4. Mapear Entity → DTO
        return UsuarioDto(
            id=usuario.id,
            nombre=usuario.nombre,
            apellido=usuario.apellido,
            mail=usuario.mail,
            celular=usuario.celular
        )

    @staticmethod
    def listar_usuario(session: Session) -> list[UsuarioDto]:
        """
        Devuelve todas los usuario.

        No devuelve entidades.
         Devuelve DTOs.
        """

        statement = select(Usuario)
        usuarios = session.exec(statement).all()

        return [
           UsuarioDto(
            id=usuario.id,
            nombre=usuario.nombre,
            apellido=usuario.apellido,
            mail=usuario.mail,
            celular=usuario.celular
        )
            for usuario in usuarios
        ]

    @staticmethod
    def obtener_usuario_por_id(
        session: Session, usuario_id: int
    ) -> UsuarioDto | None:
        """
        Busca un usuario por ID.
        Si no existe:
        - Devuelve None
        - El router decide qué HTTP status usar
        """

        usuario = session.get(Usuario, usuario_id)

        if usuario is None:
            return None

        return  UsuarioDto(
            id=usuario.id,
            nombre=usuario.nombre,
            apellido=usuario.apellido,
            mail=usuario.mail,
            celular=usuario.celular
        )

    @staticmethod
    def editar_usuario(
        session: Session, usuario_edit: UsuarioEdit
    ) -> UsuarioDto | None:
        """
        Edita una usuario existente.
        """

        usuario = session.get(Usuario, usuario_edit.id)

        if usuario is None:
            return None

        usuario.mail = usuario_edit.mail
        usuario.celular = usuario_edit.celular

        session.add(usuario)
        session.commit()
        session.refresh(usuario)

        return UsuarioDto(
            id=usuario.id,
            nombre=usuario.nombre,
            apellido=usuario.apellido,
            mail=usuario.mail,
            celular=usuario.celular
        )

    @staticmethod
    def eliminar_usuario(session: Session, usuario_id: int) -> bool:
        """
        Elimina un usuario.

        Retorna:
        - True si se eliminó
        - False si no existía
        """

        usuario = session.get(Usuario, usuario_id)

        if usuario is None:
            return False

        session.delete(usuario)
        session.commit()

        return True

   
   