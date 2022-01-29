from site import venv
from tkinter import *
from tkinter import messagebox as Messagebox

ventana = Tk()
ventana.config(bd=70)

def sacarAlerta():
    Messagebox.showinfo("Alerta", "Hola soy Capello")

Button(ventana, text="Mostrar alerta!! ", command = sacarAlerta).pack()

def salir(nombre):
    resultado = Messagebox.askquestion("Salir", "Continuar ejecutando la aplicación?")

    if resultado != "yes":
        Messagebox.showinfo("Adios!! ", f"Adios {nombre}")
        ventana.destroy()


Button(ventana, text="Salir!! ", command =lambda: salir("capello")).pack()

ventana.mainloop()