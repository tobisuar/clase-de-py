from tkinter import *


root = Tk()

miframe = Frame(root, width= 500, height= 400)

miframe.pack()
miImagen = PhotoImage(file="F:\Cursos Python videos\clase de py en videos\graficas\denji.gif")

Label(miframe, image=miImagen).place(x=100 ,y= 100)

root.mainloop()