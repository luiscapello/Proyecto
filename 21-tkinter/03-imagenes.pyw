from email.mime import image
from tkinter import *
from PIL import Image, ImageTk

ventana = Tk()
ventana.geometry("700x500")

Label(ventana, text="Bienvenido").pack(anchor=W)

imagen = Image.open('./21-tkinter/img/UYEDA.png')
render = ImageTk.PhotoImage(imagen)

Label(ventana, image=render).pack()

ventana.mainloop()