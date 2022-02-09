from cProfile import label
from tkinter import *

ventana = Tk()
ventana.geometry("400x300")
ventana.title("Formulario Uyeda")
#ventana.iconbitmap("./img/rocket-ship.ico")

# Texto Encabazado
encabezado = Label(ventana, text="Formularios || Capello")
encabezado.config(
    fg="black",
    bg="Teal",
    font=("Bahar", 20),
    padx=10,
    pady=10

)
encabezado.grid(row=0, column=0, columnspan=12, sticky=W)

#label para e campo (nombre)
label= Label(ventana, text="Nombre")
label.grid(row=1, column=0, padx=5, pady=5, sticky=W)

# Campo de texto (nombre)
campo_texto = Entry(ventana)
campo_texto.grid(row=1, column=1,sticky=W, padx=5, pady=5)
campo_texto.config(justify="right", state="normal")

#label para e campo (apellido)
label= Label(ventana, text="Apellidos")
label.grid(row=2, column=0, padx=5, pady=5, sticky=W)

# Campo de texto (apellidos)
campo_texto = Entry(ventana)
campo_texto.grid(row=2, column=1, sticky=W, padx=5, pady=5)
campo_texto.config(justify="left", state="normal")

#label para el campo (descripcion)
label = Label(ventana, text="Descripción")
label.grid(row=3, column=0, sticky=N, padx=5, pady=5)

#campo de texto grande(descripcion)
campo_grande = Text(ventana)
campo_grande.grid(row=3, column=1)
campo_grande.config(
    width=20,
    height=5,
    font=("Arial",12),
    padx=15,
    pady=15
)

#boton
Label(ventana).grid(row=4, column=1)

boton = Button(ventana, text="Enviar")
boton.grid(row=5, column=1, sticky=W)
boton.config(
    padx=5, 
    pady=5, 
    bg="SteelBlue", 
    fg="black",
    font=("Bahar", 12)
)

ventana.mainloop()