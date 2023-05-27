import sqlite3

conexion = sqlite3.connect('video_club.db')
cursor = conexion.cursor()

def insertar_registro():
    codigo = int(input("Ingrese el código de la película: "))
    titulo = input("Ingrese el título de la película: ")
    genero = input("Ingrese el género de la película: ")
    duracion = int(input("Ingrese la duración de la película (en minutos): "))
    director = input("Ingrese el director de la película: ")

    cursor.execute('INSERT INTO peliculas VALUES (?, ?, ?, ?, ?)', (codigo, titulo, genero, duracion, director))
    conexion.commit()

    print("Registro insertado exitosamente.")

def bucle():
    respuesta = input("¿Desea ingresar otro registro? (s/n): ")
    return respuesta.lower() == 's'

continuar = True
while continuar:
    insertar_registro()
    continuar = bucle()

conexion.close()



