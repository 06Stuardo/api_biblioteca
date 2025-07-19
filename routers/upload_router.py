from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from controllers.upload_controller import insertar_archivo_en_tabla

router = APIRouter(prefix="/upload", tags=["upload"])

@router.post("/importar")
async def importar_archivo(
    tabla: str = Form(...),
    file: UploadFile = File(...)
):
    try:
        return await insertar_archivo_en_tabla(file, tabla)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
