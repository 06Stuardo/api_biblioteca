SINONIMOS_CAMPOS = {
    # Nombre y apellido
    "nombre": "nombre",
    "nombres": "nombre",
    "apellido": "apellido",
    "apellidos": "apellido",

    # Correo y teléfono
    "correo": "correo",
    "correos": "correo",
    "telefono": "telefono",
    "telefonos": "telefono",

    # Claves / contraseñas
    "contrasenia": "contrasenia",
    "contrasenias": "contrasenia",
    "contraseña": "contrasenia",
    "contraseñas": "contrasenia",
    "clave": "contrasenia",
    "claves": "contrasenia",
    "password": "contrasenia",
    "passwords": "contrasenia",

    # Libros
    "titulo": "titulo",
    "titulos": "titulo",
    "isbn": "isbn",
    "anio": "aniopublicacion",
    "año": "aniopublicacion",
    "años": "aniopublicacion",
    "aniopublicacion": "aniopublicacion",
    "copias": "copiasdisponibles",
    "copiasdisponibles": "copiasdisponibles",
    "anos": "aniopublicacion",

    # Autores
    "fechanacimiento": "fechanacimiento",
    "fechasdenacimiento": "fechanacimiento",
    "nacionalidad": "nacionalidad",
    "nacionalidades": "nacionalidad",

    # Categoría
    "categoria": "nombre",
    "categorias": "nombre",

    # Prestamos
    "id": "id",
    "usuario": "id_usuario",
    "usuarios": "id_usuario",
    "libro": "id_libro",
    "libros": "id_libro",
    "fechaprestamo": "fechaprestamo",
    "prestamo": "fechaprestamo",
    "fechadeprestamo": "fechaprestamo",
    "prestamofecha": "fechaprestamo",
    "fechadevolucion": "fechadevolucion",
    "devolucion": "fechadevolucion",
    "fechadevoluciones": "fechadevolucion",
    "estado": "estado",
    "estatus": "estado",
    "condicion": "estado",
    # Prestamos
    "prestamos": "fechaprestamo",
    "fecha prestamo": "fechaprestamo",
    "fechaprestamo": "fechaprestamo",
}


SINONIMOS_TABLAS = {
    "usuarios": "usuarios",
    "autores": "autores",
    "libros": "libros",
    "categorias": "categorias",
    "prestamos": "prestamos"
}

JOIN_RELATIONS = {
    ("usuarios", "prestamos"): "usuarios.UsuarioID = prestamos.UsuarioID",
    ("libros", "prestamos"): "libros.LibroID = prestamos.LibroID",
    ("libros", "autores"): "libros.AutorID = autores.AutorID",
    ("libros", "categorias"): "libros.CategoriaID = categorias.CategoriaID",
}

JOIN_RELATIONS.update({
    (b, a): v for (a, b), v in JOIN_RELATIONS.items()
})

def get_join_clause(tabla1, tabla2):
    return JOIN_RELATIONS.get((tabla1, tabla2))

