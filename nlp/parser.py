import ply.yacc as yacc
from .lexer_rules import tokens
from .relaciones import SINONIMOS_CAMPOS, SINONIMOS_TABLAS, get_join_clause

# Ignorar artículos opcionales
def p_ignore_article(p):
    '''ignore : EL
              | LA
              | LOS
              | LAS
              | LO'''
    pass

def p_ignore_opt(p):
    '''ignore_opt : ignore'''
    pass

def p_ignore_opt_empty(p):
    '''ignore_opt : empty'''
    pass

def p_empty(p):
    '''empty :'''
    pass

# Lista de campos
def p_field_list_single(p):
    '''field_list : STRING'''
    p[0] = [SINONIMOS_CAMPOS.get(p[1].lower(), p[1].lower())]

def p_field_list_comma(p):
    '''field_list : field_list COMMA STRING'''
    p[0] = p[1] + [SINONIMOS_CAMPOS.get(p[3].lower(), p[3].lower())]

def p_field_list_y(p):
    '''field_list : field_list Y STRING'''
    p[0] = p[1] + [SINONIMOS_CAMPOS.get(p[3].lower(), p[3].lower())]

def p_field_list_comma_y(p):
    '''field_list : field_list COMMA Y STRING'''
    p[0] = p[1] + [SINONIMOS_CAMPOS.get(p[4].lower(), p[4].lower())]

# Agrupación de campos con tabla
def p_field_table_pair(p):
    '''field_table : field_list DE STRING'''
    tabla = SINONIMOS_TABLAS.get(p[3].lower(), p[3].lower())
    p[0] = [(p[1], tabla)]

def p_field_table_pair_and(p):
    '''field_table : field_table Y field_list DE STRING'''
    tabla = SINONIMOS_TABLAS.get(p[5].lower(), p[5].lower())
    p[0] = p[1] + [(p[3], tabla)]

# Condiciones (WHERE)
def p_condition(p):
    '''condition : DONDE condition_list'''
    p[0] = p[2]

def p_condition_list_simple(p):
    '''condition_list : STRING SEA STRING'''
    campo = SINONIMOS_CAMPOS.get(p[1].lower(), p[1].lower())
    valor = p[3].lower()
    p[0] = f"{campo} LIKE '%{valor}%'"

def p_condition_list_and(p):
    '''condition_list : condition_list Y STRING SEA STRING'''
    campo = SINONIMOS_CAMPOS.get(p[3].lower(), p[3].lower())
    valor = p[5].lower()
    p[0] = f"{p[1]} AND {campo} LIKE '%{valor}%'"

def p_condition_list_or(p):
    '''condition_list : condition_list O STRING SEA STRING'''
    campo = SINONIMOS_CAMPOS.get(p[3].lower(), p[3].lower())
    valor = p[5].lower()
    p[0] = f"{p[1]} OR {campo} LIKE '%{valor}%'"

def p_condition_opt(p):
    '''condition_opt : condition'''
    p[0] = p[1]

def p_condition_opt_empty(p):
    '''condition_opt : empty'''
    p[0] = None

# Consulta principal
def p_query_mostrar(p):
    '''query : SHOW ignore_opt field_table condition_opt'''
    selecciones = []
    tablas_usadas = []

    for campos, tabla in p[3]:
        selecciones.extend([f"{tabla}.{campo}" for campo in campos])
        tablas_usadas.append(tabla)

    from_clause = f"FROM {tablas_usadas[0]}"
    for i in range(1, len(tablas_usadas)):
        join_clause = get_join_clause(tablas_usadas[i - 1], tablas_usadas[i])
        if join_clause:
            from_clause += f" JOIN {tablas_usadas[i]} ON {join_clause}"
        else:
            from_clause += f", {tablas_usadas[i]}"  # fallback

    campos_sql = ', '.join(selecciones)
    condicion = f" WHERE {p[4]}" if p[4] else ""
    p[0] = f"SELECT {campos_sql} {from_clause}{condicion}"

def p_query_count(p):
    '''query : COUNT ignore_opt field_table condition_opt'''
    tablas_usadas = []
    count_field = 'id'  # Puedes cambiar este campo por uno más representativo si lo deseas

    for campos, tabla in p[3]:
        tablas_usadas.append(tabla)

    from_clause = f"FROM {tablas_usadas[0]}"
    for i in range(1, len(tablas_usadas)):
        join_clause = get_join_clause(tablas_usadas[i - 1], tablas_usadas[i])
        if join_clause:
            from_clause += f" JOIN {tablas_usadas[i]} ON {join_clause}"
        else:
            from_clause += f", {tablas_usadas[i]}"

    condicion = f" WHERE {p[4]}" if p[4] else ""
    p[0] = f"SELECT COUNT({count_field}) {from_clause}{condicion}"

def p_query_contar(p):
    '''query : COUNT STRING
             | COUNT STRING condition'''
    tabla = SINONIMOS_TABLAS.get(p[2].lower(), p[2].lower())
    alias = f"total_{tabla}"

    if len(p) == 3:
        p[0] = f"SELECT COUNT(*) AS {alias} FROM {tabla}"
    else:
        p[0] = f"SELECT COUNT(*) AS {alias} FROM {tabla} WHERE {p[3]}"

# Errores
def p_error(p):
    if p:
        print(f"Error de sintaxis en '{p.value}'")
    else:
        print("Error de sintaxis: fin de entrada inesperado")

parser = yacc.yacc(start='query')
