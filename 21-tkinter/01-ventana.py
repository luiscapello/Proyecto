from cProfile import label
from tkinter import *
import os.path

#crear la ventana raiz
ventana = Tk()

#titulo e la ventana
ventana.title("Login uyeda")

#comprobar si existe un archivo
ruta_icono = os.path.abspath('./img/rocket-ship.ico')

#Icono de la ventana
#ventana.iconbitmap(ruta_icono)

if not os.path.isfile(ruta_icono):
    ruta_icono = os.path.abspath('./21-tkinter/img/rocket-ship.ico')

#mostrar texto en el programa
texto = Label(ventana, text=ruta_icono)
texto.pack()

#cambio en el tamaño de la ventana
ventana.geometry("650x500")

#bloquear el tamaño de la ventana
ventana.resizable(0,0)



#arrancar y mostrar la ventana hasta que se cierre
ventana.mainloop()