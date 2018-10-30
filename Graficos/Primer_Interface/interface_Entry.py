from tkinter import *

root = Tk()

miFrame = Frame(root, width=1200, height=600)
miFrame.pack()


cuadroTexto = Entry(miFrame)
cuadroTexto.grid(row=0, column=1)
nombreLabel = Label(miFrame,text="Nombre")
nombreLabel.grid(row=0, column=0)

cuadroTexto = Entry(miFrame)
cuadroTexto.grid(row=1, column=1)
nombreLabel = Label(miFrame,text="Apellido")
nombreLabel.grid(row=1, column=0)

cuadroTexto = Entry(miFrame)
cuadroTexto.grid(row=2, column=1)
nombreLabel = Label(miFrame,text="Direccion")
nombreLabel.grid(row=2, column=0)

root.mainloop()