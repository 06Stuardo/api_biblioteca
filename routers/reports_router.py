from fastapi import APIRouter
from controllers.query_controller import obtener_reportes_con_resultado

router = APIRouter(prefix="/reportes", tags=["reportes"])

@router.get("/resultados")
def listar_reportes_con_resultado():
    return obtener_reportes_con_resultado()