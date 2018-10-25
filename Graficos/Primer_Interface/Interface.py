from tkinter import *

raiz =  Tk()
raiz.title("Ventana de pruebas")
# raiz.resizable(True, False)
# raiz.geometry("650x350")
raiz.config(bg="blue")

miFrame = Frame()
miFrame.pack(side="right")
miFrame.config(width="650", height="350")
miFrame.config(bg="red")

raiz.mainloop()

