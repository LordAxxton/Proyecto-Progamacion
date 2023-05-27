import sqlite3

conexion = sqlite3.connect('video_club.db')
cursor = conexion.cursor()

def mostrar_registros():
    cursor.execute('SELECT * FROM peliculas')
    resultados = cursor.fetchall()

    for fila in resultados:
        print("Código: ", fila[0])
        print("Título: ", fila[1])
        print("Género: ", fila[2])
        print("Duración: ", fila[3])
        print("Director: ", fila[4])
        print()

def mostrar_campos():
    cursor.execute('PRAGMA table_info(peliculas)') 

    #Busqué por internet una forma para que me mostrara
    #los campos disponibles al elegir la opción 2 del menú de consultas
    #y encontré información aquí: https://devdocs.io/sqlite/pragma#pragma_table_xinfo ; https://www.sqlite.org/pragma.html#pragma_table_info
   
    resultados = cursor.fetchall()

    print("Campos disponibles:")
    for fila in resultados:
        print(fila[1])
    print()

opcion = input("Ingrese el criterio de consulta (1 - Código, 2 - Otro campo, 3 - Mostrar todos los registros): ")

if opcion == '1':
    codigo = int(input("Ingrese el código de la película: "))
    cursor.execute('SELECT * FROM peliculas WHERE codigo = ?', (codigo,))
elif opcion == '2':
    mostrar_campos()
    campo = input("Ingrese el nombre del campo a consultar: ")
    valor = input("Ingrese el valor a buscar en el campo {}: ".format(campo))
    cursor.execute('SELECT * FROM peliculas WHERE lower({}) = ?'.format(campo), (valor,))
elif opcion == '3':
    mostrar_registros()

resultados = cursor.fetchall()

for fila in resultados:
    print("Código: ", fila[0])
    print("Título: ", fila[1])
    print("Género: ", fila[2])
    print("Duración: ", fila[3])
    print("Director: ", fila[4])
    print()

conexion.close()