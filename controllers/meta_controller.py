from fastapi import HTTPException, status
from db.connection import get_connection
from datetime import datetime, timedelta, timezone

def listar_tablas():
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        SELECT TABLE_NAME
        FROM INFORMATION_SCHEMA.TABLES
        WHERE TABLE_TYPE = 'BASE TABLE'
          AND TABLE_CATALOG = 'BD_Biblioteca';
    """
    print(query)
    cursor.execute(query)
    result = cursor.fetchall()

    return [row[0] for row in result]