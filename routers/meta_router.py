from fastapi import APIRouter
from controllers.meta_controller import *

router = APIRouter(prefix="/meta", tags=["metadata"])

@router.get("/tables")
def list_tables():
    return listar_tablas()