import pytest
import ply.lex as lex
import nlp.lexer_rules as lexer_rules


@pytest.mark.parametrize("entrada, tipo_esperado", [
    ("mostrar", "SHOW"),
    ("contar", "COUNT"),
    ("donde", "DONDE"),
    ("libros", "STRING"),
    (",", "COMMA"),
])
def test_reconocimiento_tokens(entrada, tipo_esperado):
    lexer = lex.lex(module=lexer_rules)
    lexer.input(entrada)

    token = lexer.token()

    assert token is not None
    assert token.type == tipo_esperado
    assert lexer.token() is None


def test_reconocimiento_sea():
    lexer = lex.lex(module=lexer_rules)
    lexer.input("sea")

    token = lexer.token()

    assert token is not None
    assert token.type == "SEA"
    assert lexer.token() is None


def test_caracter_ilegal(capsys):
    lexer = lex.lex(module=lexer_rules)
    lexer.input("#")

    assert lexer.token() is None
    salida = capsys.readouterr()
    assert "Caracter ilegal: #" in salida.out
