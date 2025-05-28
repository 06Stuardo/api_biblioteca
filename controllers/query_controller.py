from db.connection import get_connection

def ejecutar_query(sql: str) -> list[dict] | dict:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(sql)
        columns = [col[0] for col in cursor.description]
        rows = cursor.fetchall()
        return [dict(zip(columns, row)) for row in rows]
    except Exception as e:
        return {"error": str(e)}

def guardar_reporte(nombre: str, consulta: str):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO reportes (nombre, consulta_sql)
            VALUES (?, ?)
        """, (nombre, consulta))
        conn.commit()
    except Exception as e:
        print("Error al guardar el reporte:", e)

from db.connection import get_connection

def obtener_reportes_con_resultado():
    resultados = []
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT nombre, consulta_sql FROM reportes")
        reportes = cursor.fetchall()

        for nombre, consulta in reportes:
            try:
                cur = conn.cursor()
                cur.execute(consulta)
                columnas = [col[0] for col in cur.description]
                filas = cur.fetchall()
                data = [dict(zip(columnas, fila)) for fila in filas]
                resultados.append({"nombre": nombre.upper(), "resultado": data})
            except Exception as e:
                print("Error al obtener reporte:", e)
                #resultados.append({"nombre": nombre.upper(), "error": str(e)})

        return resultados
    except Exception as e:
        return [{"error": f"Error general: {e}"}]