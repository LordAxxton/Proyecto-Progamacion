import sqlite3

conexion = sqlite3.connect('video_club.db')
cursor = conexion.cursor()

codigo = int(input("Ingrese el código de la película que desea modificar: "))

titulo = input("Ingrese el nuevo título de la película: ")
genero = input("Ingrese el nuevo género de la película: ")
duracion = int(input("Ingrese la nueva duración de la película en minutos: "))
director = input("Ingrese el nuevo director de la película: ")

cursor.execute('''
    UPDATE peliculas
    SET titulo = ?, genero = ?, duracion = ?, director = ?
    WHERE codigo = ?
''', (titulo, genero, duracion, director, codigo))

conexion.commit()
conexion.close()
print("Registro modificado exitosamente.")
