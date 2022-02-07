from distutils import command
from tkinter import *

def show_caracter():
    caracter_window = Toplevel()

game = Tk()

Button(game, text="caracter", command=show_caracter).pack()

game.mainloop()

