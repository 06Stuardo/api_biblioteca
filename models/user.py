from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Usuario(BaseModel):
    UsuarioID: int
    Nombre: str
    Apellido: str
    Correo: str
    Telefono: Optional[str] = None
    FechaRegistro: datetime
    Contrasenia: Optional[str] = None