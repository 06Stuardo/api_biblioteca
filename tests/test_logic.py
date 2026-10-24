import pytest
from nlp.logic import normalizar_entrada


@pytest.mark.parametrize("entrada, esperado", [
    ("MOSTRAR LIBROS", "mostrar libros"),
    ("Mostrar correo electronico", "mostrar correo"),
    ("Mostrar clave secreta", "mostrar contrasenia"),
    ("Mostrar   libros", "mostrar libros"),
    ("¿Mostrar libros?", "mostrar libros"),
])
def test_normalizar_entrada(entrada, esperado):
    assert normalizar_entrada(entrada) == esperado

from unittest.mock import patch
from nlp.logic import text_to_sql


def test_text_to_sql_consulta_valida():
    with patch("nlp.logic.parser.parse", return_value="SELECT * FROM libros") as mock_parser:
        resultado = text_to_sql("MOSTRAR LIBROS")
        assert resultado == "SELECT * FROM libros"
        mock_parser.assert_called_once_with("mostrar libros")


def test_text_to_sql_consulta_no_interpretada():
    with patch("nlp.logic.parser.parse", return_value=None):
        resultado = text_to_sql("MOSTRAR LIBROS")
        assert resultado == "No se pudo interpretar la consulta."


def test_text_to_sql_error_parser():
    with patch("nlp.logic.parser.parse", side_effect=ValueError("Error de prueba")):
        resultado = text_to_sql("MOSTRAR LIBROS")
        assert resultado == "Error: Error de prueba"


def test_normalizar_correo_con_tilde():
    assert normalizar_entrada("Mostrar correo electrónico") == "mostrar correo"
