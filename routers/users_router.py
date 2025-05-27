from tokenize import String

from fastapi import APIRouter
from db.connection import get_connection
from models.user import Usuario

router = APIRouter(prefix="/usuarios", tags=["usuarios"])


@router.get("/listaUsuario", response_model=list[Usuario])
def listar_usuarios():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT UsuarioID, Nombre, Apellido, Correo, Telefono, FechaRegistro, Contrasenia FROM Usuarios")
    rows = cursor.fetchall()
    conn.close()

    usuarios = [
        {
            "UsuarioID": row[0],
            "Nombre": row[1],
            "Apellido": row[2],
            "Correo": row[3],
            "Telefono": row[4],
            "FechaRegistro": row[5],
            "Contrasenia": row[6]
        }
        for row in rows
    ]
    return usuarios
@router.get("/inicio")
def mensaje_inicio():
    return 'Primer API en python'