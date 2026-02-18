from fastapi import APIRouter, Depends, HTTPException,  status
from sqlmodel import Session
from core.database import get_session
from schemas.usuario import UsuarioCreate, UsuarioDto, UsuarioEdit
from services.usuario_service import UsuarioService

router = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios"]
)



@router.post(
    "/",  
    response_model=UsuarioDto,          
    status_code=status.HTTP_201_CREATED   
)
def crear(
    usuario: UsuarioCreate , session: Session = Depends(get_session)
):
    """
    Crea un nuevo Usuario.
    """

    return UsuarioService.crear_usuario(session, usuario)


@router.get("/", response_model=list[UsuarioDto])
def listar_usuario(session: Session = Depends(get_session)):
    """
    Devuelve todas los Usuarios.
    """

    return UsuarioService.listar_usuario(session)

@router.get("/{usuario_id}", response_model=UsuarioDto)
def busca_por_id(usuario_id:int, session: Session = Depends(get_session)):
    """
    Devuelve usuario por id
    """
    usuario =  UsuarioService.obtener_usuario_por_id(session, usuario_id )

    if usuario is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado"
        )
    return usuario

@router.put("/", response_model=UsuarioDto)
def editar_usuario(usuario_edit: UsuarioEdit, session: Session = Depends(get_session)):
    """
    Docstring for editar_usuario
    
    :param usuario_edit: Description
    :type usuario_edit: UsuarioEdit
    :param session: Description
    :type session: Session
    """
    usuario_editado = UsuarioService.editar_usuario(session, usuario_edit)
    if usuario_editado is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="usuario no encontrado"
        )
    return usuario_editado

@router.delete("/{usuario_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_categoria(usuario_id: int, session: Session = Depends(get_session)):
    """
    Elimina una usuario por ID.
    """

    eliminado = UsuarioService.eliminar_usuario(session, usuario_id)

    if not eliminado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrada"
        )
