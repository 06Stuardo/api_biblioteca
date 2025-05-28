from fastapi import APIRouter
from nlp.logic import text_to_sql
from models.query import QueryRequest
from controllers.query_controller import *

router = APIRouter(prefix="/query", tags=["query"])

@router.post("/convert")
def convert_to_sql(req: QueryRequest):
    sql = text_to_sql(req.question)
    resultado = ejecutar_query(sql)
    if resultado is not None:
        guardar_reporte(nombre=req.nombre_reporte, consulta=sql)

    return {"sql": sql, "data": resultado}




