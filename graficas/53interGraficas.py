from tkinter import *
from tkinter import ttk
from typing import Sized
#siempre se puede buscar la libreria online buscando tkinter python 3
raiz=Tk()
raiz.title("Ventana de prueba")
raiz.size()

#creacion de frame
#frm = ttk.Frame(raiz, padding = 10)
#frm.grid()
#ttk.Label(frm, text= "Hola mundo").grid(column=0,row=0)
#ttk.Button(frm,text="quit", command=raiz.destroy).grid(column=1,row=0)

#creacion de frame 2
miframe = Frame()
miframe.pack(side=LEFT, anchor="n")
miframe.config(bg="grey")
miframe.config(width="150",height="100")
miframe.config(bd=2)
miframe.config(relief="groove")

raiz.geometry("720x480")#tamaño de la interface
raiz.config(bg="")#cambio de color
raiz.mainloop()
