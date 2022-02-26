import tkinter as tk
from PIL import ImageTk, Image
import pandas as pd

# Loading the DataFrame caracter file
caracters = pd.read_csv("data/caracters.csv", index_col="Name")
types_dict = {
    "To_fire": "Fuego",
    "To_rock": "Roca",
    "To_water": "Agua",
    "To_electric": "Eléctrico",
    "To_plant": "Planta",
    "To_beetle": "Escarabajo",
}

class Game:
    def __init__(self, user, mode):
        self.root = tk.Tk()
        self.user = user
        self.root.title("Fightcreatures")
        self.root.geometry("636x660")
        self.root.resizable(width=False, height=False)
        self.caracters = caracters.index.tolist()
        self.mode = mode

        player = tk.Label(
            self.root,
            text=f"Jugador: {self.user}",
            font=("Verdana", 20),
            width=35,
            anchor=tk.W
        )
        player.grid(row=0, columnspan=3)

        self.display_buttons()
        self.root.mainloop()

    def caracter_button(self, name):
        caracter = tk.Button(
            self.root,
            text="Detalle",
            pady=5,
            font=("Arial", 12),
            command=lambda: ShowCaracter(name),
            )
        return caracter

    def caracter_label(self, name):
        caracter = tk.Label(
            self.root,
            text=name,
            pady=5,
            font=("Arial", 12),
            )
        return caracter

    def show_panel(self, name):
        image_path = caracters.loc[name, "Picture"]
        img = Image.open(image_path)
        img = img.resize((200,200), Image.ANTIALIAS)
        photoImg =  ImageTk.PhotoImage(img)
        panel = tk.Button(
            self.root,
            bd= 5,
            image = photoImg,
            relief="raised"
        )
        panel.image = photoImg
        
        return panel

    def display_buttons(self):
        dupla = zip(self.caracters, range(len(self.caracters)))
        for caracter, i in dupla:
            caracter_name = self.caracter_label(caracter)
            panel = self.show_panel(caracter)
            c_buton = self.caracter_button(caracter)
            if i == 0:
                caracter_name.grid(row=1, column=0)
                panel.grid(row=2, column=0)
                c_buton.grid(row=3, column=0)
            elif i == 1:
                caracter_name.grid(row=1, column=1)
                panel.grid(row=2, column=1)
                c_buton.grid(row=3, column=1)
            elif i == 2:
                caracter_name.grid(row=1, column=2)
                panel.grid(row=2, column=2)
                c_buton.grid(row=3, column=2)
            elif i == 3:
                caracter_name.grid(row=4, column=0)
                panel.grid(row=5, column=0)
                c_buton.grid(row=6, column=0)
            elif i == 4:
                caracter_name.grid(row=4, column=1)
                panel.grid(row=5, column=1)
                c_buton.grid(row=6, column=1)
            elif i == 5:
                caracter_name.grid(row=4, column=2)
                panel.grid(row=5, column=2)
                c_buton.grid(row=6, column=2)
        
        start = tk.Button(
            self.root,
            text="INICIAR",
            pady=10,
            padx=10,
            font=("Arial", 12),
        )
        start.grid(row=7, columnspan=3)


class ShowCaracter:
    def __init__(self, name):
        self.root = tk.Toplevel()
        self.root.geometry("860x480")
        self.name = name
        self.root.title(name + " info")
        self.root.resizable(width=False, height=False)
        self.display_content()

    def display_content(self):
        self.stats_title(0)
        self.show_panel().grid(row=1, rowspan=3, column=0, columnspan=3)
        self.show_advantage().grid(row=1,  column=3, columnspan=4)
        self.show_disadvantage().grid(row=2,  column=3, columnspan=4)
        self.show_normal().grid(row=3,  column=3, columnspan=4)
        self.table()
        
    def table(self):

        def table_by_labels(columns, row):
            columns_plus = zip(columns, range(len(columns)))
            for i, j in columns_plus:
                single_column = tk.Label(
                    self.root,
                    text=i,
                    font=("Arial", 12)
                )
                if i == caracters.loc[self.name, "Description"]:
                    single_column.grid(row=row, column=j, columnspan=6)
                if i == "Ataque\nnormal":
                    single_column.config(width=10)
                single_column.grid(row=row, column=j)

        row_1 = (
            "Habilida",
            "Ataque\nnormal",
            "Ataque con\nventaja",
            "Ataque con\ndesventaja",
            "Ataque con\npotenciador\nnormal",
            "Ataque con\npotenciador con\nventaja",
            "Ataque con\npotenciador con\ndesventaja"
        )
        row_2 = (caracters.loc[self.name, "Attack_1"], "3", "5", "2", "5", "7", "4")
        row_3 = (caracters.loc[self.name, "Attack_2"], caracters.loc[self.name, "Attack_power"])
        row_4 = (caracters.loc[self.name, "Attack_2"], caracters.loc[self.name, "Attack_power"])
        row_5 = (caracters.loc[self.name, "Attack_3"], caracters.loc[self.name, "Attack_power"])
        row_6 = (caracters.loc[self.name, "Special"],  caracters.loc[self.name, "Description"])

        list_of_rows = [row_1, row_2, row_3, row_4, row_5, row_6]

        def table_generator(list_of_rows, start):
            rows_plus = zip(list_of_rows, range(len(list_of_rows)))
            for row, row_number in rows_plus:
                row_start = row_number + start
                table_by_labels(row, row_start)

        return table_generator(list_of_rows, 4)


    def stats_title(self, row):
        
        caracter_name_type = tk.Label(
            self.root,
            text=f"{self.name}",
            font=("Arial", 20)
        )
        
        caracter_type = tk.Label(
            self.root,
            text=f"Tipo: {caracters.loc[self.name, 'Type']}",
            font=("Arial", 20)
        )
        
        caracter_name_type.grid(row=row, column=0, columnspan=3)
        caracter_type.grid(row=row, column=3, columnspan=4)
    
    def show_panel(self):
        
        image_path = caracters.loc[self.name, "Picture"]
        img = Image.open(image_path)
        img = img.resize((250,250), Image.ANTIALIAS)
        photoImg =  ImageTk.PhotoImage(img)
        panel = tk.Label(self.root, image = photoImg)
        panel.image = photoImg
        
        return panel
    
    def modifiers(self):
        
        advantage = []
        disadvantage = []
        normal = []
        
        colums = caracters.columns.tolist()
        for col in colums:
            if col != "Attack_power":
                if caracters.loc[self.name, col] == 2:
                    advantage.append(col)
                elif caracters.loc[self.name, col] == -1:
                    disadvantage.append(col)
                elif caracters.loc[self.name, col] == 0:
                    normal.append(col)               
        
        list_of_buffs = advantage + disadvantage + normal
        correct_types = []
        
        for buff in list_of_buffs:
            correct_types.append(types_dict[buff])
        
        return correct_types

    def show_advantage(self):
        stats = self.modifiers()
        advantage = tk.Label(
            self.root,
            text=f"\tVentaja con:\t\t{stats[0]+ ', ' + stats[1]}.",
            font=("Arial", 15),
            anchor='w',
            height=2,
            width=50
        )
        return advantage

    def show_disadvantage(self):
        stats = self.modifiers()
        disadvantage = tk.Label(
            self.root,
            text=f"\tDesventaja con:\t\t{stats[2] + ', ' + stats[3]}.",
            font=("Arial", 15),
            anchor='w',
            height=2,
            width=50
        )
        return disadvantage

    def show_normal(self):
        stats = self.modifiers()
        normal = tk.Label(
            self.root,
            text=f"\tNormal con:\t\t{stats[4]+ ', ' + stats[5]}.",
            font=("Arial", 15),
            anchor='w',
            height=2,
            width=50
        )
        return normal


if __name__ == "__main__":
    Game("Marco", "mode1")
