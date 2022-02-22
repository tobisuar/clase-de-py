from cProfile import label
from cgitb import text
from operator import ge
from tkinter import *

root = Tk()

varOpcion = IntVar()

def imprimir():

    #print(varOpcion.get())

    if varOpcion.get()==1:

        etiqueta.config(text="elegiste masculino")

    elif varOpcion.get()==2:

        etiqueta.config(text="elegiste femenino")
    

Label(root,text="Genero:").pack()

Radiobutton(root, text="Masculino",variable=varOpcion, value=1, command=imprimir ).pack()

Radiobutton(root, text="Femenino",variable=varOpcion, value=2, command=imprimir ).pack()

etiqueta = Label(root)
etiqueta.pack()


root.mainloop()