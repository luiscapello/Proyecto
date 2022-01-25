from tkinter import *
from tkinter import messagebox as Messagebox

ventana = Tk()
ventana.config(bd=70)

def sacarAlerta():
    Messagebox.showinfo("Alerta", "Hola soy Capello")

Button(ventana, text="Mostrar alerta!! ", command = sacarAlerta).pack()

ventana.mainloop()