from tkinter import *

#crear la ventana raiz
ventana = Tk()

#titulo e la ventana
ventana.title("Login uyeda")

#cambio en el tamaño de la ventana
ventana.geometry("750x500")

#bloquear el tamaño de la ventana
ventana.resizable(0,0)

#Icono de la ventana
ventana.iconbitmap("./21-tkinter/img/rocket-ship.ico")

#arrancar y mostrar la ventana hasta que se cierre
ventana.mainloop()