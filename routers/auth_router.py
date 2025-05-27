# routers/auth_router.py

from fastapi import APIRouter
from models.login_request import LoginRequest
from controllers.auth_controller import *

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login")
def login(datos: LoginRequest):
    return verificar_credenciales(datos.username, datos.password)