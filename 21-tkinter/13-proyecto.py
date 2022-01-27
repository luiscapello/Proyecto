from cmath import inf
from tkinter import *

#definir ventana
ventana = Tk()
ventana.geometry("500x600")
ventana.title("proyecto Tkinter")
ventana.resizable(0,0)

#pantallas
def home():
    home_label = Label(ventana, text="Inicio")
    home_label.config(
        fg="white",
        bg="black",
        font=("Arial", 20),
        padx=20,
        pady=20
    )
    home_label.grid(row=0, column=0)

    return True

def add():
    add_label = Label(ventana, text="Agregar Producto")
    add_label.config(
        fg="white",
        bg="black",
        font=("Arial", 20),
        padx=20,
        pady=20
    )
    add_label.grid(row=0, column=0)
    return True

def info():
    info_label = Label(ventana, text="Información")
    info_label.config(
        fg="white",
        bg="black",
        font=("Arial", 20),
        padx=20,
        pady=20
    )
    info_label.grid(row=0, column=0)

    data_label = Label(ventana, text="Creado por Capello - 27-01-2022")
    data_label.grid(row=1, column=0)
    return True

#cargar pantalla iicio
home()

#menu superiro
menu_superior = Menu(ventana)
menu_superior.add_command(label="Inicio", command=home)
menu_superior.add_command(label="Añadir", command=add)
menu_superior.add_command(label="Información", command=info)
menu_superior.add_command(label="Salir", command=ventana.quit)

#cargar menu
ventana.config(menu=menu_superior)

#cargar ventana
ventana.mainloop()