import mysql.connector

#conexión
database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "master_python"
)

# conexion correcta?
# print(database)

# cursor
cursor = database.cursor()

# crear base de datos

cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

cursor.execute("SHOW DATABASES")

for db in cursor:
    print(db)

# Crear tablas
cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos(
    id int(10) auto_increment not null,
    marca varchar(40) not null,
    modelo varchar(40) not null,
    precio varchar(40) not null,
    CONSTRAINT pk_vehiculo PRIMARY KEY(id)
)
""")

# mostrar tables en consola
"""
cursor.execute("SHOW TABLES")

for table in cursor:
     print(table)


#insertar datos
#cursor.execute("INSERT INTO vehiculos VALUES(null, 'Opel', 'Astra', 18500)")

#insertar varios datos
coches = [
    ('Seat', 'Ibiza', 5000),
    ('Renault', 'Clio', 3000),
    ('Citroen', 'Saxo', 7000),
    ('Mercedes', 'Clese C', 15000),
    ('Volkswagen', 'Jetta', 9000)
]
#cursor.executemany("INSERT INTO vehiculos VALUES (null, %s, %s, %s)" , coches)

database.commit()

#mostrar datos
cursor.execute("SELECT * FROM vehiculos")

result = cursor

print("---- Todos Mis Coches ----")
for coches in result:
    print(coches)

#borrar datos

cursor.execute("DELETE FROM vehiculos WHERE marca = 'Mercedes'")
database.commit()

print(cursor.rowcount, "Borrados!!")

#actualizar datos

cursor.execute("UPDATE vehiculos SET modelo = 'C4 PureTech 155' WHERE marca = 'Citroen'")
database.commit()

print(cursor.rowcount, "Actualizados!!")
"""