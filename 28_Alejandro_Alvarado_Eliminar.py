import sqlite3

conexion = sqlite3.connect('video_club.db')
cursor = conexion.cursor()

def eliminar_registro():
    codigo = int(input("Ingrese el código de la película que desea eliminar: "))

    cursor.execute('SELECT * FROM peliculas WHERE codigo = ?', (codigo,))
    resultado = cursor.fetchone()

    if resultado:
        cursor.execute('DELETE FROM peliculas WHERE codigo = ?', (codigo,))
        conexion.commit()
        print("Registro eliminado con éxito.")
    else:
        print("Registro inexistente.")

def continuar_eliminar():
    respuesta = input("¿Desea eliminar otro registro? (s/n): ")
    return respuesta.lower() == 's'

continuar = True
while continuar:
    eliminar_registro()
    continuar = continuar_eliminar()

conexion.close()
