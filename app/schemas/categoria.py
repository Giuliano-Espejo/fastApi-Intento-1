
from pydantic import BaseModel

class CategoriaCreate(BaseModel):
    """
    Equivalente a CategoriaCreate.java

    Se usa para:
    - Crear una categoría
    - Recibir datos desde el frontend
    """

    nombre: str
class CategoriaEdit(BaseModel):
    """
    Equivalente a CategoriaEdit.java

    Se usa para:
    - Editar una categoría existente
    """

    id: int
    nombre: str

class CategoriaDto(BaseModel):
    """
    Equivalente a CategoriaDto.java

    Se usa para:
    - Respuestas al frontend
    """

    id: int
    nombre: str
    

