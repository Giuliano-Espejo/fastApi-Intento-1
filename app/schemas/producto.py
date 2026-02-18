
from pydantic import BaseModel

class ProductoCreate(BaseModel):
    """
    DTO para crear productos.

    Coincide con el ProductoCreate.java
    """

    nombre: str
    precio: float
    stock: int
    categoria_id: int

class ProductoDto(BaseModel):
    """
    DTO para productos.

    Coincide con el ProductoDTO.java
    """
    id: int
    nombre: str
    precio: float
    stock: int
    categoria_id: int

class ProductoEdit(BaseModel):
    id:int
    nombre: str
    precio: float
    stock: int

