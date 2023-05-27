import sqlite3

conexion = sqlite3.connect('video_club.db')
cursor = conexion.cursor()

cursor.execute('''
    CREATE TABLE peliculas (
        codigo INTEGER PRIMARY KEY,
        titulo TEXT,
        genero TEXT,
        duracion INTEGER,
        director TEXT
    )
''')

conexion.commit()
conexion.close()
print("Base de datos creada exitosamente.")

