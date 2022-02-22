from tkinter import *

root = Tk()

root.title("Ejemplo")

playa = IntVar()
mountain = IntVar()
turismo = IntVar()

def opcionesViaje():

    opcionesEscogidas = ""

    if (playa.get()==1):
        opcionesEscogidas+= " Playa"

    if (mountain.get()==1):
        opcionesEscogidas+= " Montaña"

    if (turismo.get()==1):
        opcionesEscogidas+= " Turismo Rural"

    textofinal.config(text=opcionesEscogidas)

#foto = PhotoImage(file ="F:\Cursos Python videos\clase de py en videos\avion.png")
#Label(root, Image = foto).pack()

frame= Frame(root)
frame.pack()

Label(frame, text="Elige destinos", width=50).pack()

Checkbutton(root, text="Playa",variable=playa, onvalue=1,offvalue=0,command=opcionesViaje).pack()
Checkbutton(root, text="Montaña",variable=mountain, onvalue=1,offvalue=0,command=opcionesViaje).pack()
Checkbutton(root, text="Turismo Rural",variable=turismo,onvalue=1,offvalue=0,command=opcionesViaje).pack()

textofinal = Label(frame)
textofinal.pack()


root.mainloop()