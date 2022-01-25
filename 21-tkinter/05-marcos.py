from tkinter import *

ventana = Tk()
ventana.title("Marcos || capello")
ventana.geometry("400x500")

marco_padre = Frame(ventana, width=150, height=200)
marco_padre.pack(side=BOTTOM, anchor=S, fill=X, expand=YES)

marco = Frame(marco_padre, width=150, height=200)
marco.config(
    bg="Teal",
    bd=3,
    relief=SOLID
)
marco.pack(side=LEFT, anchor=SW)

marco = Frame(marco_padre, width=150, height=200)
marco.config(
    bg="DarkTurquoise",
    bd=3,
    relief=SOLID
)
marco.pack(side=RIGHT, anchor=SE)

marco_padre = Frame(ventana, width=150, height=200)
marco_padre.pack(side=TOP,anchor=N, fill=X, expand=YES)

marco = Frame(marco_padre, width=150, height=200)
marco.config(
    bg="Maroon",
    bd=3,
    relief=SOLID
)
marco.pack(side=LEFT)

marco = Frame(marco_padre, width=150, height=200)
marco.config(
    bg="YellowGreen",
    bd=3,
    relief=SOLID
)
marco.pack(side=RIGHT)



ventana.mainloop()