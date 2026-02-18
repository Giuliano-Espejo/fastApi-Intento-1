from pydantic import BaseModel
class UsuarioLogin(BaseModel):
    """
    DTO para logear usuarios.
    """

    nombre: str
    email: str


class UsuarioDto(BaseModel):
    """
    DTO de salida del usuario.
    """

    id: int
    nombre: str
    email: str

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
    mail: str
    celular: int

