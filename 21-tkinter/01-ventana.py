from cProfile import label
from tkinter import *
import os.path

class Programa:

    def __init__(self):
        self.title = "Login Uyeda Industrial de mexico"
        self.icon = './img/rocket-ship.ico'
        self.icon_alt = './21-tkinter/img/rocket-ship.ico'
        self.size = "650x500"
        self.resizable = False

    def cargar(self):
        #crear la ventana raiz
        ventana = Tk()
        self.ventana = ventana

        #titulo e la ventana
        ventana.title(self.title)

        #comprobar si existe un archivo
        ruta_icono = os.path.abspath(self.icon)

        #Icono de la ventana
        #ventana.iconbitmap(ruta_icono)

        if not os.path.isfile(ruta_icono):
            ruta_icono = os.path.abspath(self.icon_alt)

        #mostrar texto en el programa
        texto = Label(ventana, text=ruta_icono)
        texto.pack()

        #cambio en el tamaño de la ventana
        ventana.geometry(self.size)

        #bloquear el tamaño de la ventana
        if self.resizable:
            ventana.resizable(1,1)
        else:
            ventana.resizable(0,0)

    def addtexto(self):
        texto = Label(self.ventana, text="Ingresa al sistema")
        texto.pack()

    def mostrar(self):
        #arrancar y mostrar la ventana hasta que se cierre
        self.ventana.mainloop()

# Instanciar programa
programa = Programa()
programa.cargar()
programa.addtexto()
programa.mostrar()
