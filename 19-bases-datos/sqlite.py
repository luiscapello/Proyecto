import sqlite3

#conexion
conexion = sqlite3.connect('./19-bases-datos/pruebas.db')

#crear cursor
cursor = conexion.cursor()

#crear tablas
cursor.execute("CREATE TABLE IF NOT EXISTS productos("+
    "id INTEGER PRIMARY KEY AUTOINCREMENT,"+
    "titulo varchar(255),"+
    "descripcion text,"+
    "precio int(255)"+
")")

#guardar cambios
conexion.commit()

#insertar datos
cursor.execute("INSERT INTO productos VALUES (null,'Primer Producto', 'Descripción de mi producto', 550)")
conexion.commit()

# listar datos
cursor.execute("SELECT * FROM productos;")
productos = cursor.fetchall()

for producto in productos:
    print(producto)

#cerrar conexion
conexion.close()