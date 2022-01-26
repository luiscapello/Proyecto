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
    return True

def info():
    return True

#cargar pantalla iicio
home()

#menu superiro
menu_superior = Menu(ventana)
menu_superior.add_command(label="Inicio")
menu_superior.add_command(label="Añadir")
menu_superior.add_command(label="Información")
menu_superior.add_command(label="Salir", command=ventana.quit)

#cargar menu
ventana.config(menu=menu_superior)

#cargar ventana
ventana.mainloop()