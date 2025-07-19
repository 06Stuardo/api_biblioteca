from fastapi import APIRouter, HTTPException
from controllers.etl_controller import obtener_todas_las_tablas_etl

router = APIRouter(prefix="/etl", tags=["etl"])

@router.get("/reportes")
def get_all_etl_tables():
    try:
        return obtener_todas_las_tablas_etl()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))