from .parser import parser
import logging

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

    # Reemplazar frases compuestas → tokens unidos que el lexer entienda como un solo STRING
    compuestas = {
        "fechas de nacimiento": "fechasdenacimiento",
        "fecha de nacimiento": "fechasdenacimiento",
        "nombres completos": "nombrescompletos",
        "numero de documento": "numerodocumento",
        "nombre completo": "nombrecompleto",
        "correo electronico": "correo",
        "direcciones de correo": "correos",
        "clave secreta": "contrasenia",
    }

    for frase, reemplazo in compuestas.items():
        texto = texto.replace(frase, reemplazo)

    # Opcional: limpieza de tildes, símbolos, doble espacios, etc. (solo si lo necesitas)
    texto = texto.replace("á", "a").replace("é", "e").replace("í", "i")
    texto = texto.replace("ó", "o").replace("ú", "u")
    texto = ' '.join(texto.split())  # quita dobles espacios

    return texto
