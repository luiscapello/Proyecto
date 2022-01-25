from tkinter import *

ventana = Tk()
ventana.geometry("600x500")
ventana.config(
    bd=50
)

def getDato():
    resultado.set(dato.get())

    if len(resultado.get()) >= 1:
        texto_recogido.config(
            bg="SeaGreen",
            fg="white"
        )

dato = StringVar()
resultado = StringVar()

Label(ventana, text="Ingresa el texto: ").pack(anchor=NW)
Entry(ventana, textvariable=dato).pack(anchor=NW)

Label(ventana, text="Dato recogido: ").pack(anchor=NW)
texto_recogido = Label(ventana, textvariable=resultado)


texto_recogido.pack(anchor=NW)

Button(ventana, text="Mostrar dato", command=getDato).pack(anchor=NW)


ventana.mainloop()