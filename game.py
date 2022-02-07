from tkinter import *
from PIL import ImageTk, Image
import pandas as pd

caracters = pd.read_csv("data/caracters.csv", index_col="Name")

def show_caracter(name):
    caracter_window = Toplevel()
    image_path = caracters.loc[name, "Picture"]
    print(image_path)
    img = ImageTk.PhotoImage(file=image_path)
    
    panel = Label(caracter_window, image = img)
    panel.image = img
    panel.grid(row=0, column=0)
    
    type = caracters.loc[name, "Type"]
    Name = Label(caracter_window, text=f"{name}:").grid(row=1, column=0)
    Type = Label(caracter_window, text=f"Tipo {type}").grid(row=1, column=1)

game = Tk()

Aquarder = Button(game, text="Aquarder", command=lambda: show_caracter("Aquarder"))
Firesor = Button(game, text="Firesor", command=lambda: show_caracter("Firesor"))
Electder = Button(game, text="Electder", command=lambda: show_caracter("Electder"))
Mousebug = Button(game, text="Mousebug", command=lambda: show_caracter("Mousebug"))
Splant = Button(game, text="Splant", command=lambda: show_caracter("Splant"))
Rockdog = Button(game, text="Rockdog", command=lambda: show_caracter("Rockdog"))

Aquarder.grid(row=0, column=0)
Firesor.grid(row=0, column=1)
Electder.grid(row=0, column=2)
Mousebug.grid(row=1, column=0)
Splant.grid(row=1, column=1)
Rockdog.grid(row=1, column=2)

game.mainloop()
