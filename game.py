from calendar import c
import tkinter as tk
from PIL import ImageTk, Image
import pandas as pd

# Loading the DataFrame caracter file
caracters = pd.read_csv("data/caracters.csv", index_col="Name")

class Game:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("400x200")
        self.root.title("Battlemon")
        self.root.geometry("800x600")
        self.w_h_fs(40, 32, 12)
        self.caracters = ["Aquarder", "Firesor", "Electder", "Mousebug", "Splant", "Rockdog"]
        self.display_buttons()
        self.root.mainloop()
    
    def w_h_fs(self, w, h, fs):
        self.width = w
        self.height = h
        self.font_size = fs

    def caracter_button(self, name):
        caracter = tk.Button(
            self.root,
            text=name,
            padx=60,
            pady=20,
            font=("Arial", 12),
            command=lambda: show_caracter(name),
            )
        return caracter


    def display_buttons(self):
        dupla = zip(self.caracters, range(len(self.caracters)))
        for caracter, i in dupla:
            c_buton = self.caracter_button(caracter)
            if i == 0:
                c_buton.grid(row=0, column=0)
            elif i == 1:
                c_buton.grid(row=0, column=1)
            elif i == 2:
                c_buton.grid(row=0, column=2)
            elif i == 3:
                c_buton.grid(row=1, column=0)
            elif i == 4:
                c_buton.grid(row=1, column=1)
            elif i == 5:
                c_buton.grid(row=1, column=2)


def show_caracter(name):
    caracter_window = tk.Toplevel()
    image_path = caracters.loc[name, "Picture"]
    print(image_path)
    img = ImageTk.PhotoImage(file=image_path)
    
    panel = tk.Label(caracter_window, image = img)
    panel.image = img
    panel.grid(row=0, columnspan=6)
    
    type = caracters.loc[name, "Type"]
    caracter_name = tk.Label(caracter_window, text=f"{name}:").grid(row=1, column=3)
    caracter_type = tk.Label(caracter_window, text=f"Tipo {type}").grid(row=1, column=4)
    caracter_ability = tk.Label(caracter_window, text="Habilida").grid(row=2, column=0)
    caracter_attack = tk.Label(caracter_window, text="Ataque normal").grid(row=2, column=1)
    caracter_advantage = tk.Label(caracter_window, text="Ataque con ventaja").grid(row=2, column=2)
    caracter_disadvantage = tk.Label(caracter_window, text="Ataque con desventaja").grid(row=2, column=3)
    caracter_powered = tk.Label(caracter_window, text="Ataque con potenciador normal").grid(row=2, column=4)
    caracter_powered_advantage = tk.Label(caracter_window, text="Ataque con potenciador con ventaja").grid(row=2, column=5)
    caracter_powered_disadvantage = tk.Label(caracter_window, text="Ataque con potenciador con desventaja").grid(row=2, column=6)


if __name__ == "__main__":
    Game()
