
from nlp import lexer_rules
from nlp.logic import normalizar_entrada
from nlp.parser import parser
from nlp.relaciones import SINONIMOS_CAMPOS, SINONIMOS_TABLAS

def analizar(texto):
    texto = normalizar_entrada(texto)
    print("📥 Entrada:", texto)
    lexer = lexer_rules.lexer
    lexer.input(texto)

    print("\n🧩 Tokens:")
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(f"  {tok.type}: {tok.value}")

    print("\n🧠 Resultado del parser:")
    try:
        resultado = parser.parse(texto, lexer=lexer)
        print("✅ SQL generado:", resultado)
    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    prueba = "listar titulos de libros y nombres de autores"
    analizar(prueba)
