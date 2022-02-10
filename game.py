import tkinter as tk
from tkinter import ttk
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

class Login:
    def __init__(self):
        self.geometry('300x150')
        self.resizable(0, 0)
        self.title('Login')

        # UI options
        paddings = {'padx': 5, 'pady': 5}
        entry_font = {'font': ('Helvetica', 11)}

        # configure the grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        username = tk.StringVar()
        password = tk.StringVar()

        # heading
        heading = ttk.Label(self, text='Member Login', style='Heading.TLabel')
        heading.grid(column=0, row=0, columnspan=2, pady=5, sticky=tk.N)

        # username
        username_label = ttk.Label(self, text="Username:")
        username_label.grid(column=0, row=1, sticky=tk.W, **paddings)

        username_entry = ttk.Entry(self, textvariable=username, **entry_font)
        username_entry.grid(column=1, row=1, sticky=tk.E, **paddings)

        # password
        password_label = ttk.Label(self, text="Password:")
        password_label.grid(column=0, row=2, sticky=tk.W, **paddings)

        password_entry = ttk.Entry(
            self, textvariable=password, show="*", **entry_font)
        password_entry.grid(column=1, row=2, sticky=tk.E, **paddings)

        # login button
        login_button = ttk.Button(self, text="Login")
        login_button.grid(column=1, row=3, sticky=tk.E, **paddings)

        # configure style
        self.style = ttk.Style(self)
        self.style.configure('TLabel', font=('Helvetica', 11))
        self.style.configure('TButton', font=('Helvetica', 11))

        # heading style
        self.style.configure('Heading.TLabel', font=('Helvetica', 12))

class Game:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("400x200")
        self.root.title("Battlemon")
        self.root.geometry("800x600")
        self.caracters = caracters.index.tolist()
        self.display_buttons()
        self.root.mainloop()


    def caracter_button(self, name):
        caracter = tk.Button(
            self.root,
            text=name,
            width=20,
            padx=40,
            pady=20,
            font=("Arial", 12),
            command=lambda: ShowCaracter(name),
            )
        return caracter

    def show_panel(self):
        
        image_path = caracters.loc[self.name, "Picture"]
        img = Image.open(image_path)
        img = img.resize((200,200), Image.ANTIALIAS)
        photoImg =  ImageTk.PhotoImage(img)
        panel = tk.Label(self.root, image = photoImg)
        panel.image = photoImg
        
        return panel

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


class ShowCaracter:
    def __init__(self, name):
        self.root = tk.Toplevel()
        self.root.geometry("840x400")
        self.name = name
        self.root.title(name + " info")
        #self.root.resizable(width=False, height=False)
        self.display_content()

    def display_content(self):
        self.stats_title(0)
        self.show_panel().grid(row=1, rowspan=3, column=0)
        self.show_advantage().grid(row=1,  column=1)
        self.show_disadvantage().grid(row=2,  column=1)
        self.show_normal().grid(row=3,  column=1)
        self.table().grid(row=4,column=0, columnspan=2)
        
    def table(self):

        style = ttk.Style()
        style.configure(" Treeview.Heading ", rowheight=10, background="red")

        columns = (
            "Habilida",
            "Ataque normal",
            "Ataque con\nventaja",
            "Ataque con\ndesventaja",
            "Ataque con\npotenciador\nnormal",
            "Ataque con\npotenciador con\nventaja",
            "Ataque con\npotenciador con\ndesventaja"
        )
        
        info_table = ttk.Treeview(self.root, height=5)
        info_table["columns"] = columns
        info_table.column("#0", width=0, stretch=tk.NO)
        for col in columns:
            info_table.column(col, anchor=tk.CENTER, width=120, minwidth=25)
            info_table.heading(col, text=col, anchor=tk.CENTER)
            

        info_table.insert(
            parent='',
            index=tk.END,
            values=(
                caracters.loc[self.name, "Attack_1"],
                "3",
                "5",
                "2",
                "5",
                "7",
                "4"
            )
        )
        
        info_table.insert(
            parent='',
            index=tk.END,
            values=(
                caracters.loc[self.name, "Attack_2"],
                caracters.loc[self.name, "Attack_power"]
            )
        )
        
        info_table.insert(
            parent='',
            index=tk.END,
            values=(
                caracters.loc[self.name, "Attack_3"],
                caracters.loc[self.name, "Attack_power"]
            )
        )
        
        info_table.insert(
            parent='',
            index=tk.END,
            values=(
                caracters.loc[self.name, "Special"],
                caracters.loc[self.name, "Description"]
            )
        )

        return info_table

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
        
        caracter_name_type.grid(row=row, column=0)
        caracter_type.grid(row=row, column=1)
    
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
            text=f"Ventaja con: {stats[0]+ ' , ' + stats[1]}.",
            font=("Arial", 15),
            bg="#D3D3D3",
            height=2,
            width=50
        )
        return advantage

    def show_disadvantage(self):
        stats = self.modifiers()
        disadvantage = tk.Label(
            self.root,
            text=f"Desventaja con: {stats[2] + ' , ' + stats[3]}.",
            font=("Arial", 15),
            bg="#D3D3D3",
            height=2,
            width=50
        )
        return disadvantage

    def show_normal(self):
        stats = self.modifiers()
        normal = tk.Label(
            self.root,
            text=f"Normal con: {stats[4]+ ' , ' + stats[5]}.",
            font=("Arial", 15),
            bg="#D3D3D3",
            height=2,
            width=50
        )
        return normal


if __name__ == "__main__":
    Game()
