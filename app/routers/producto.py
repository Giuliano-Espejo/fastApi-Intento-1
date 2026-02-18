from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
# APIRouter: permite agrupar endpoints por recurso
# Depends: inyección de dependencias (Session, auth, etc.)
# HTTPException: errores HTTP explícitos
# status: constantes HTTP legibles

from core.database import get_session
from services.producto_service import ProductoService
from schemas.producto import ProductoCreate, ProductoDto, ProductoEdit
# get_session: nos da una Session por request
# CategoriaService: lógica de negocio
# schemas: contrato con el frontend (DTOs).


router = APIRouter(prefix="/productos", tags=["Productos"])



@router.post(
    "/",  
    response_model=ProductoDto,          
    status_code=status.HTTP_201_CREATED   
)
def crear(
    producto: ProductoCreate, session: Session = Depends(get_session)
):
    """
    Crea una nueva categoría.
    """

    return ProductoService.crear_producto(session, producto)


@router.get("/", response_model=list[ProductoDto])
def listar_producto(session: Session = Depends(get_session)):
    """
    Devuelve todas las categorías.
    """

    return ProductoService.listar_productos(session)

@router.get("/{producto_id}", response_model=ProductoDto)
def busca_por_id(producto_id:int, session: Session = Depends(get_session)):
    """
    Devuelve producto por id
    """
    producto=  ProductoService.obtener_producto_por_id(session, producto_id )

    if producto is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Categoría no encontrada"
        )
    return producto

@router.put("/", response_model=ProductoDto)
def editar_producto(producto_edit: ProductoEdit, session: Session = Depends(get_session)):
    """
    Docstring for editar_producto
    
    :param producto_edit: Description
    :type producto_edit: ProductoEdit
    :param session: Description
    :type session: Session
    """
    producto_editado = ProductoService.editar_producto(session, producto_edit)
    if producto_editado is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="producto no encontrado"
        )
    return producto_editado

@router.delete("/{producto_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_categoria(producto_id: int, session: Session = Depends(get_session)):
    """
    Elimina una categoría por ID.
    """

    eliminado = ProductoService.eliminar_producto(session, producto_id)

    if not eliminado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Producto no encontrada"
        )
