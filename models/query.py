from pydantic import BaseModel

class QueryRequest(BaseModel):
    question: str
    nombre_reporte: str