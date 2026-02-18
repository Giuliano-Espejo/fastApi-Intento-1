from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
# APIRouter: permite agrupar endpoints por recurso
# Depends: inyección de dependencias (Session, auth, etc.)
# HTTPException: errores HTTP explícitos
# status: constantes HTTP legibles

from core.database import get_session
from services.categoria_service import CategoriaService
from schemas.categoria import CategoriaCreate, CategoriaEdit, CategoriaDto
# get_session: nos da una Session por request
# CategoriaService: lógica de negocio
# schemas: contrato con el frontend (DTOs).


router = APIRouter(prefix="/categorias", tags=["Categorías"])



@router.post(
    "/",  
    response_model=CategoriaDto,          # Forma exacta de la respuesta, en caso de que se agregue algo 
                                          # que no sea de "CategoriaDTO" se obviara por fastapi y no sera
                                          # parte de la respuesta 
    status_code=status.HTTP_201_CREATED   # Código HTTP correcto para creación
)
def crear(
    categoria: CategoriaCreate, session: Session = Depends(get_session)
):
    """
    Crea una nueva categoría.
    """

    return CategoriaService.crear_categoria(session, categoria)


@router.get("/name", response_model=CategoriaDto)
def obtener_categoria_por_nombre(categoria_nombre: str, session: Session = Depends(get_session)):
    """
    Devuelve una categoría por ID.
    """

    categoria = CategoriaService.obtener_categoria_por_nombre(session, categoria_nombre)

    if categoria is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Categoría no encontrada"
        )

    return categoria

@router.get("/", response_model=list[CategoriaDto])
def listar_categorias(session: Session = Depends(get_session)):
    """
    Devuelve todas las categorías.
    """

    return CategoriaService.listar_categorias(session)


@router.get("/{categoria_id}", response_model=CategoriaDto)
def obtener_categoria(categoria_id: int, session: Session = Depends(get_session)):
    """
    Devuelve una categoría por ID.
    """

    categoria = CategoriaService.obtener_categoria_por_id(session, categoria_id)

    if categoria is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Categoría no encontrada"
        )

    return categoria


@router.put("/", response_model=CategoriaDto)
def editar_categoria(categoria: CategoriaEdit, session: Session = Depends(get_session)):
    """
    Edita una categoría existente.
    """

    categoria_editada = CategoriaService.editar_categoria(session, categoria)

    if categoria_editada is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Categoría no encontrada"
        )

    return categoria_editada


@router.delete("/{categoria_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_categoria(categoria_id: int, session: Session = Depends(get_session)):
    """
    Elimina una categoría por ID.
    """

    eliminado = CategoriaService.eliminar_categoria(session, categoria_id)

    if not eliminado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Categoría no encontrada"
        )


