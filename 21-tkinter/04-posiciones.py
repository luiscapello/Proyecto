from tkinter import *
from tkinter import font

ventana = Tk()
#ventana.geometry("650x450")
#ventana.resizable(0,0)

texto = Label(ventana, text=" Bienvenido  al  sistema  de  Uyeda")
texto.config(
    fg="white",
    bg="black",
    padx=70,
    pady=20,
    font=("Bahar", 25),
    cursor="trek"
)
texto.pack(side= TOP)

texto = Label(ventana, text=" capello")
texto.config(
    fg="black",
    bg="orange",
    padx=30,
    pady=20,
    font=("Arial", 25),
    cursor="trek"
)
texto.pack(side=TOP, fill=X, expand=YES)

texto = Label(ventana, text=" basico")
texto.config(
    fg="black",
    bg="red",
    padx=30,
    pady=20,
    font=("Arial", 25),
    cursor="trek"
)
texto.pack(side=LEFT, fill=X, expand=YES)

texto = Label(ventana, text=" basico")
texto.config(
    fg="black",
    bg="Fuchsia",
    padx=30,
    pady=20,
    font=("Arial", 25),
    cursor="trek"
)
texto.pack(side=LEFT, fill=X, expand=YES)

texto = Label(ventana, text=" basico")
texto.config(
    fg="black",
    bg= "Teal",
    padx=30,
    pady=20,
    font=("Arial", 25),
    cursor="trek"
)
texto.pack(side=LEFT, fill=X, expand=YES)

ventana.mainloop()