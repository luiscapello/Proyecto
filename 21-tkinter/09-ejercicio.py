"""
    calculadora con dos campos de texto
    4 botones para las operaciones
    mostrar el resultado en una alerta
"""

from tkinter import *
from tkinter import messagebox

ventana = Tk()
ventana.title("Ejercicio con tkinter || calculadora || Capello")
ventana.geometry("400x400")
ventana.resizable(0,0)
ventana.config(bd=25)

def sumar():
    try:
        resultado.set(float(numero1.get()) + float(numero2.get()))
        mostrarResultado()
    except:
        messagebox.showerror("Error", "Introduce solo numero..")
        numero1.set("")
        numero2.set("")

def restar():
    try:
        resultado.set(float(numero1.get()) - float(numero2.get()))
        mostrarResultado()
    except:
        messagebox.showerror("Error", "Introduce solo numero..")
        numero1.set("")
        numero2.set("")

def multiplicar():
    try:
        resultado.set(float(numero1.get()) * float(numero2.get()))
        mostrarResultado()
    except:
        messagebox.showerror("Error", "Introduce solo numero..")
        numero1.set("")
        numero2.set("")


def dividir():
    try:
        resultado.set(float(numero1.get()) / float(numero2.get()))
        mostrarResultado()
    except:
        messagebox.showerror("Error", "Introduce solo numero..")
        numero1.set("")
        numero2.set("")

def mostrarResultado():
    messagebox.showinfo("Resultado..", f"El resultado de la operacion es: {resultado.get()}")
    numero1.set("")
    numero2.set("")


numero1 = StringVar()
numero2 = StringVar()
resultado = StringVar()

marco = Frame(ventana, width=500, height=600)
marco.config(
    bd=5,
    relief=SOLID,
    padx=20,
    pady=20
)
marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(False)

Label(marco, text="Primer numero: ").pack()
Entry(marco, textvariable = numero1, justify="center").pack()

Label(marco, text="Segundo numero: ").pack()
Entry(marco, textvariable = numero2, justify="center").pack()

Label(marco, text="").pack()

Label(marco, text="").pack(side="left")
Button(marco, text=" Sumar ", command=sumar).pack(side="left", fill=X, expand=YES)
Label(marco, text="").pack(side="left")
Button(marco, text=" Restar ", command=restar).pack(side="left", fill=X, expand=YES)
Label(marco, text="").pack(side="left")
Button(marco, text=" Multiplicar ", command=multiplicar).pack(side="left", fill=X, expand=YES)
Label(marco, text="").pack(side="left")
#Button(marco, text=" Dividir ", command=dividir).pack(side="left", fill=X, expand=YES)
#Label(marco, text="").pack(side="left")

ventana.mainloop()