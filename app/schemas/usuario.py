from pydantic import BaseModel

class UsuarioDto(BaseModel):
    """
    DTO de salida del usuario.
    """

    id: int
    nombre: str
    apellido:str
    mail: str
    celular: int

class UsuarioCreate(BaseModel):
    """
    DTO de creacion del usuario.
    """

    nombre: str
    apellido:str
    mail: str
    celular: int
    contrasena: str

class UsuarioEdit(BaseModel):
    id: int
    mail: str
    celular: int

