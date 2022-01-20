from tkinter import *
from tkinter import font

ventana = Tk()
ventana.geometry("650x450")
ventana.resizable(0,0)

texto = Label(ventana, text=" Bienvenido  al  sistema  de  Uyeda")
texto.config(
    fg="white",
    bg="black",
    padx=70,
    pady=20,
    font=("Bahar", 25),
    cursor="trek"
)
texto.pack()

ventana.mainloop()