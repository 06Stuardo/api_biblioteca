import pandas as pd
import io
from fastapi import UploadFile
from db.connection import get_connection

async def insertar_archivo_en_tabla(file: UploadFile, tabla: str):
    nombre = file.filename
    extension = nombre.split('.')[-1].lower()
    content = await file.read()

    # Leer el archivo
    if extension == 'csv':
        df = pd.read_csv(io.StringIO(content.decode('utf-8')))
    elif extension in ['xlsx', 'xls']:
        df = pd.read_excel(io.BytesIO(content))
    else:
        raise ValueError("Formato no soportado")

    # Insertar en la base de datos
    conn = get_connection()
    cursor = conn.cursor()

    columnas = ','.join(df.columns)
    placeholders = ','.join(['?' for _ in df.columns])
    query = f"INSERT INTO {tabla} ({columnas}) VALUES ({placeholders})"


    for _, fila in df.iterrows():

        cursor.execute(query, tuple(fila))

    conn.commit()
    cursor.close()
    conn.close()

    return {"mensaje": f"{len(df)} registros insertados en {tabla}"}
