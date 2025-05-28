from .parser import parser
import logging
import re

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def text_to_sql(texto: str) -> str:
    try:
        texto = normalizar_entrada(texto)
        logger.info("Texto normalizado: %s", texto)
        resultado = parser.parse(texto)
        return resultado or "No se pudo interpretar la consulta."
    except Exception as e:
        return f"Error: {str(e)}"

def normalizar_entrada(texto: str) -> str:
    texto = texto.lower()

    # Reemplazos personalizados
    reemplazos = {
        "fechas de nacimiento": "fechasdenacimiento",
        "fecha de nacimiento": "fechasdenacimiento",
        "correo electronico": "correo",
        "clave secreta": "contrasenia",
        "fecha prestamo": "fechaprestamo",
        "fecha de prestamo": "fechaprestamo",
        "sean":"sea"
    }

    for frase, reemplazo in reemplazos.items():
        texto = texto.replace(frase, reemplazo)

    # Palabras y símbolos a ignorar
    palabras_ignoradas = [
        "sus", "su", "del", "de los", "de las", "las", "los", "el", "la", "hay"
    ]
    for palabra in palabras_ignoradas:
        texto = re.sub(rf'\b{palabra}\b', '', texto)

    # Eliminar signos de interrogación
    texto = texto.replace("¿", "").replace("?", "")
    # Eliminar dobles espacios
    texto = re.sub(r'\s+', ' ', texto).strip()

    # Opcional: limpieza de tildes, símbolos, doble espacios, etc. (solo si lo necesitas)
    texto = texto.replace("á", "a").replace("é", "e").replace("í", "i")
    texto = texto.replace("ó", "o").replace("ú", "u")
    texto = ' '.join(texto.split())  # quita dobles espacios
    print(texto)
    return texto
