import ply.yacc as yacc
from .lexer_rules import tokens

# Diccionarios para normalizar
SINONIMOS_CAMPOS = {
    "titulos": "titulo",
    "nombres": "nombre",
    "apellidos": "apellido",
    "correos": "correo",
    "contraseñas": "contrasenia",
    "contrasenias": "contrasenia",
    "passwoerd": "contrasenia",
    "telefonos": "telefono",
    "teléfonos": "telefono",
    "fechas de nacimiento": "fechaNacimiento",
    "nacionalidades": "nacionalidad",
    "fechasdenacimiento": "fechaNacimiento",
    "nacionalidad": "nacionalidad",
}

SINONIMOS_TABLAS = {
    "libro": "libros",
    "usuario": "usuarios",
    "prestamo": "prestamos",
    "usuarios": "usuarios",
    "libros": "libros",
    "prestamos": "prestamos",
    "autores": "autores"
}


# Artículos ignorables
def p_ignore_article_el(p): 'ignore : EL'; pass
def p_ignore_article_los(p): 'ignore : LOS'; pass
def p_ignore_article_las(p): 'ignore : LAS'; pass
def p_ignore_article_lo(p): 'ignore : LO'; pass

def p_ignore_opt(p):
    '''ignore_opt : ignore
                  | empty'''
    pass

def p_empty(p): 'empty :'; pass

# Lista de campos
def p_field_list_single(p):
    'field_list : STRING'
    p[0] = [SINONIMOS_CAMPOS.get(p[1].lower(), p[1].lower())]

def p_field_list_multi(p):
    '''field_list : field_list COMMA STRING
                  | field_list Y STRING
                  | field_list COMMA Y STRING
                  | field_list O STRING'''
    p[0] = p[1] + [SINONIMOS_CAMPOS.get(p[len(p) - 1].lower(), p[len(p) - 1].lower())]

# Condiciones múltiples con LIKE
def p_condition(p):
    'condition : DONDE condition_list'
    p[0] = p[2]

def p_condition_list(p):
    '''condition_list : STRING SEA STRING
                      | condition_list Y STRING SEA STRING
                      | condition_list O STRING SEA STRING'''
    if len(p) == 4:
        campo = SINONIMOS_CAMPOS.get(p[1].lower(), p[1].lower())
        valor = p[3].lower()
        p[0] = f"{campo} LIKE '%{valor}%'"
    else:
        operador = 'AND' if p[2].lower() == 'y' else 'OR'
        campo = SINONIMOS_CAMPOS.get(p[3].lower(), p[3].lower())
        valor = p[5].lower()
        p[0] = f"{p[1]} {operador} {campo} LIKE '%{valor}%'"

def p_condition_opt(p):
    '''condition_opt : condition
                     | empty'''
    p[0] = p[1] if len(p) > 1 else None

# Consulta completa
def p_query_mostrar_varios(p):
    'query : SHOW ignore_opt field_list DE STRING condition_opt'
    campos = ', '.join(p[3])
    tabla = SINONIMOS_TABLAS.get(p[5].lower(), p[5].lower())
    where = f" WHERE {p[6]}" if p[6] else ""
    p[0] = f"SELECT {campos} FROM {tabla}{where}"

def p_error(p):
    if p:
        print(f"Error de sintaxis en '{p.value}'")
    else:
        print("Error de sintaxis: fin de entrada inesperado")

parser = yacc.yacc(start='query')