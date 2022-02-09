from cgitb import text
from cmath import inf
from tkinter import *

#definir ventana
ventana = Tk()
ventana.geometry("500x450")
ventana.title("Uyeda Industrial de Mexico")
ventana.resizable(0,0)
ventana.config(
    bg="Teal"
)
#pantallas
def home():
    
    home_label.config(
        fg="white",
        bg="black",
        font=("Arial", 20),
        padx=220,
        pady=20
    )
    home_label.grid(row=0, column=0)

    #ocultar pantallas
    add_label.grid_remove()
    #add_frame.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()

    return True

def add():
    #encabezado
    add_label.config(
        fg="white",
        bg="black",
        font=("Arial", 20),
        padx=145,
        pady=20
    )
    add_label.grid(row=0, column=0, columnspan=8)

    #campos del formulario
    #add_frame.grid(row=1)
    add_name_label.grid(row=1, column=0, padx=5, pady=5, sticky=E)
    add_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

    add_price_label.grid(row=2, column=0, padx=5, pady=5, sticky=E)
    add_price_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)

    #add_description_label.grid(row=3, column=0, padx=5, pady=5, sticky=NE)
    #add_description_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)
    #add_description_entry.config(
     #   width=32,
      #  height=10,
       # font=("Consolas",12),
        #padx=3,
        #pady=3
    #)
    add_separator.grid(row=4)

    boton.grid(row=5, column=1, sticky=E)
    boton.config(
        pady=5,
        padx=15,
        bg="Teal",
        fg="white"
    )
    add_separator.grid(row=4)
    add_separator.grid(row=4)

    data_label = Label(ventana, text="Uyeda Industrial de Mexico Creado por Capello")

    

    #ocultar pantallas
    home_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()

    return True

def info():
    
    info_label.config(
        fg="white",
        bg="black",
        font=("Arial", 20),
        padx=180,
        pady=20
    )
    info_label.grid(row=0, column=0)

    
    data_label.grid(row=1, column=0)

    #ocultar pantallas
    add_label.grid_remove()
    #add_frame.grid_remove()
    home_label.grid_remove()

    return True

def add_product():
    products.append([
        name_data.get,
        price_data.get,
        add_description_entry.get("1.0", "end-1c")
    ])

    print(products)

# variables importantes
products = []
name_data = StringVar()
price_data = StringVar()


#definir campos de pantalla (inicio)
home_label = Label(ventana, text="Inicio")

#definir campos de pantalla (add)
add_label = Label(ventana, text="Agregar Producto")

#crear compas del formularios
#add_frame = Frame(ventana)


add_name_label = Label(ventana, text="Nombre de usurio : ")
add_name_entry = Entry(ventana, textvariable=name_data)

add_price_label = Label(ventana, text="Contraseña : ")
add_price_entry = Entry(ventana, textvariable=price_data)


add_separator = Label(ventana)

boton = Button(ventana, text="Guardar")
add_separator = Label(ventana)


#definir campos de pantalla (info)
info_label = Label(ventana, text="Información")
data_label = Label(ventana, text="Uyeda Industrial de Mexico Creado por Capello")


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