#Quitar las comillas para intercambiar como se muestra la portada

import tkinter as tk
from tkinter import font
import sqlite3

def numero_registros():
    conn = sqlite3.connect('video_club.db')
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM peliculas')
    numero_registros = cursor.fetchone()[0]
    conn.close()
    return numero_registros

""
#Portada Tkinter
def mostrar_portada():
    ventana = tk.Tk()
    ventana.title("Portada")
    ventana.geometry("550x350")

    titulo = font.Font(family="Arial", size=20, weight="bold")
    texto = font.Font(family="Times New Roman", size=13)
    mensaje = font.Font(family="Calisto MT", size=10)
    registro = font.Font(family="Times New Roman", size=7)

    titulo_label = tk.Label(ventana, text="Proyecto \n SQLite - Python", font=titulo)
    titulo_label.pack(pady=20)

    nombre_label = tk.Label(ventana, text="Nombre: Alejandro Rafael Alvarado Valenzuela", font=texto)
    nombre_label.pack()

    numero_cuenta_label = tk.Label(ventana, text="Número de Cuenta: 28", font=texto)
    numero_cuenta_label.pack()

    asignatura_label = tk.Label(ventana, text="Asignatura: Programación", font=texto)
    asignatura_label.pack()

    curso_label = tk.Label(ventana, text="Curso: 12 BTP", font=texto)
    curso_label.pack()

    fecha_label = tk.Label(ventana, text="Fecha: 8 de Junio del 2023", font=texto)
    fecha_label.pack()

    mensaje_label = tk.Label(ventana, text="Created by Alejandro Alvarado", font=mensaje)
    mensaje_label.pack(pady=45)

    numero_registros_label = tk.Label(ventana, text="Número de registros: {}".format(numero_registros()), font=registro, fg="gray")
    numero_registros_label.place(x=400, y=320)

    ventana.mainloop()

mostrar_portada()
""

"""""
# Mostrar portada en modo consola
print("Proyecto \n SQLite - Python")
print("\nNombre: Alejandro Rafael Alvarado Valenzuela")
print("Número de Cuenta: 28")
print("Asignatura: Programación")
print("Curso: 12 BTP")
print("Fecha: 8 de Junio del 2023")
print("Created by Alejandro Alvarado")
print("\nNúmero de registros: {}\n".format(numero_registros()))
"""""