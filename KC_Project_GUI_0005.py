#!/usr/bin/python3
from tkinter import *
import tkinter as ttk

#Definimos nuestra ventana principal
window = Tk()
window.title("Welcome to KeepCoding Demo App")

#Color del fondo
window.config(bg="black")

#Insertamos la imagen
photo = PhotoImage(file="penelope cruz GIF-source.gif")
label = Label(window, image=photo). place(x=40, y=20)
window.geometry("620x370")

#Definimos el enlace en caso de pulsar el boton 1
url = 'https://es.wikipedia.org/wiki/Pen%C3%A9lope_Cruz'

def enlace():
    import webbrowser
    webbrowser.open_new(url)

#Creamos los botones
boton1 = ttk.Button(window, text = "Salir", command = exit).pack(side = ttk.BOTTOM)
boton2 = ttk.Button(window, text = "Quiero saber más", command = enlace).pack(side = ttk.BOTTOM)

window.mainloop()

