# Practica label  

from tkinter import *

root = Tk()

miFrame = Frame(root, width=500, height=400)

miFrame.pack()

miLabel = Label(miFrame, text = "Hola mundo.", fg="red")
miLabel.place(x = 100, y = 200)
miLabel.pack()

root.mainloop()