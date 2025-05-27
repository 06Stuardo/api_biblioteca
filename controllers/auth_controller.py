from fastapi import HTTPException, status
from db.connection import get_connection
from datetime import datetime, timedelta, timezone
from jose import jwt

SECRET_KEY = "supersecreta"  # Usa una más segura en producción
ALGORITHM = "HS256"

def crear_token(data: dict, expires_delta: timedelta = timedelta(hours=1)):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + expires_delta
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verificar_credenciales(username: str, password: str):
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT Contrasenia FROM Usuarios WHERE Correo = ?"
    cursor.execute(query, (username,))
    result = cursor.fetchone()

    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado"
        )

    stored_password = result[0]

    if stored_password != password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Contraseña incorrecta"
        )

    # ✅ Aquí devolvemos un token
    token = crear_token({"sub": username})
    return {"access_token": token, "token_type": "bearer"}
