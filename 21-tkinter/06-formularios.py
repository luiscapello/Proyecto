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

#label para e campo
label= Label(ventana, text="Nombre")
label.grid(row=1, column=0,sticky=W, padx=5, pady=5)

# Campo de texto
campo_texto = Entry(ventana)
campo_texto.grid(row=1, column=1, sticky=W, padx=5, pady=5)
campo_texto.config(justify="right", state="normal")


ventana.mainloop()