from db.connection import get_connection_etl

def obtener_todas_las_tablas_etl():
    conn = get_connection_etl()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT TABLE_NAME
        FROM INFORMATION_SCHEMA.TABLES
        WHERE TABLE_TYPE = 'BASE TABLE'
    """)
    tablas = [row[0] for row in cursor.fetchall()]

    resultado = []

    for tabla in tablas:
        try:
            cursor.execute(f"SELECT * FROM {tabla}")
            columnas = [col[0] for col in cursor.description]
            filas = [dict(zip(columnas, row)) for row in cursor.fetchall()]

            resultado.append({
                "tabla": tabla,
                "columnas": columnas,
                "datos": filas
            })
        except Exception as e:
            resultado.append({
                "tabla": tabla,
                "error": str(e)
            })

    cursor.close()
    conn.close()

    return resultado
