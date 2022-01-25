from cProfile import label
from tkinter import *

ventana = Tk()
ventana.geometry("400x300")
ventana.title("Formulario Uyeda")

# Texto Encabazado
encabezado = Label(ventana, text="Formularios || Capello")
encabezado.config(
    fg="black",
    bg="Teal",
    font=("Bahar", 15),
    padx=10,
    pady=10

)
encabezado.grid(row=0, column=0, columnspan=12, sticky=W)

#label para e campo (nombre)
label= Label(ventana, text="Nombre")
label.grid(row=1, column=0, padx=5, pady=5)

# Campo de texto (nombre)
campo_texto = Entry(ventana)
campo_texto.grid(row=1, column=1, sticky=W, padx=5, pady=5)
campo_texto.config(justify="right", state="normal")

#label para e campo (apellido)
label= Label(ventana, text="Apellidos")
label.grid(row=2, column=0, padx=5, pady=5)

# Campo de texto (apellidos)
campo_texto = Entry(ventana)
campo_texto.grid(row=2, column=1, sticky=W, padx=5, pady=5)
campo_texto.config(justify="left", state="normal")

#label para e campo (descripcion)
label = Label(ventana, text="Descripción")
label.grid(row=3, column=0, padx=5, pady=5)

#campo de texto grande(descripcion)
campo_grande = Text(ventana)
campo_grande.grid(row=3, column=1)
campo_grande.config(
    width=30,
    height=5
)

ventana.mainloop()