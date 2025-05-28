import ply.lex as lex
import sys

tokens = [
    'SHOW', 'COUNT', 'DE', 'EL', 'LOS', 'LAS', 'LO', "LA",
    'COMMA', 'Y', 'O', 'DONDE', 'SEA', 'STRING'
]

def t_SHOW(t): r'mostrar|ver|listar|enséñame'; return t
def t_COUNT(t): r'cuántos|cuantas|contar|cuente|cuantos'; return t
def t_DE(t): r'de'; return t
def t_EL(t): r'el'; return t
def t_LOS(t): r'los'; return t
def t_LAS(t): r'las'; return t
def t_LO(t): r'lo'; return t
def t_LA(t): r'la'; return t
def t_COMMA(t): r','; return t
def t_Y(t): r'y'; return t
def t_O(t): r'o'; return t
def t_DONDE(t): r'donde|dónde|cuando'; return t

def t_SEA(t):
    r"sea|igual"
    return t

def t_STRING(t):
    r"[a-zA-Z0-9_áéíóúÁÉÍÓÚñÑ@.]+"
    return t

t_ignore = ' \t\n'

def t_error(t):
    print(f"Caracter ilegal: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex(module=sys.modules[__name__])
