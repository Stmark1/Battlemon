import tkinter as tk
import game
import csv

from tkinter import messagebox

class Start:
    
    def __init__(self, first_window):
    
        self.root = tk.Tk()
        self.root.geometry("400x400")
        self.root.title("Fightcreatures")
        self.root.resizable(width=False, height=False)
        self.user = ""
        self.users = []

        self.user_db()

        self.container = tk.Frame(self.root) 
        self.container.pack(side = "top", fill = "both", expand = True)
  
        self.container.grid_rowconfigure(0, weight = 1)
        self.container.grid_columnconfigure(0, weight = 1)
        
        self.frames = {}

        self.show_frame(first_window)

        self.root.mainloop()

    def show_frame(self, cont):
  
        self.prepare_frames()
        frame = self.frames[cont]
        frame.root.tkraise()

    def prepare_frames(self):
  
        for frame in (Login_or_register, Register, Login, SelectMode):
            page = frame(self.container, self)
            self.frames[frame] = page
            page.root.grid(row = 0, column = 0, sticky ="nsew")
    
    def user_db(self):
        
        users = []
        
        try:
            with open(r'data\users.csv', 'r') as db:
                csv_file = csv.DictReader(db)
                for row in csv_file:
                    users.append(dict(row))
                self.users = users
                db.close()
        
        except FileNotFoundError:
            with open(r'data\users.csv', 'w') as db:
                fieldnames = ['user', 'password', 'level']
                writer = csv.DictWriter(db, fieldnames=fieldnames)
                writer.writeheader()
                self.users = users
                db.close()
        

class Login_or_register:
    
    def __init__(self, parent, controller):
    
        self.root = tk.Frame(parent)
        self.controller = controller

        message = tk.Label(
            self.root,
            text="Bienvenido a Fightcreatures",
            font=("Verdana", 20),
        )
        message.grid(row=0, column=0)
        
        button1 = tk.Button(
            self.root,
            text="Ingresa",
            font=("Verdana", 20),
            command=lambda : self.controller.show_frame(Login)
        )
        button1.grid(row=1, column=0)

        button2 = tk.Button(
            self.root,
            text="Regístrate",
            font=("Verdana", 20),
            command=lambda : self.controller.show_frame(Register)
        )
        button2.grid(row=3, column=0)

class Register:
    
    def __init__(self, parent, controller):
    
        self.root = tk.Frame(parent)
        self.controller = controller

        user_label = tk.Label(self.root, text="Usuarío")
        user_label.grid(row=0, column=0)
        self.user_entry = tk.Entry(self.root, width=50)
        self.user_entry.grid(row=0, column=1)

        password_label = tk.Label(self.root, text="Contraseña")
        password_label.grid(row=1, column=0)
        self.password_entry = tk.Entry(self.root, width=50)
        self.password_entry.grid(row=1, column=1)

        password2_label = tk.Label(self.root, text="Repita la contraseña")
        password2_label.grid(row=2, column=0)
        self.password2_entry = tk.Entry(self.root, width=50)
        self.password2_entry.grid(row=2, column=1)

        sub_btn=tk.Button(self.root,text = 'Registrarse', command = self.user_register)
        sub_btn.grid(row=3, columnspan=2)

        back_btn=tk.Button(self.root,text = 'Regresar', command = self.back)
        back_btn.grid(row=4, columnspan=2)

    def back(self):

        self.controller.show_frame(Login_or_register)

    def submit(self):
        
        self.controller.user = self.user_entry.get()
        self.password = self.password_entry.get()
        self.controller.show_frame(SelectMode)

    def user_register(self):
        
        users = []
        user_name = []

        with open(r'data\users.csv', 'r') as db:
            csv_file = csv.DictReader(db)
            for row in csv_file:
                users.append(dict(row))
            self.controller.users = users
            db.close()

        for row in users:
            user_name.append(row['user'])

        self.user = self.user_entry.get()
        self.password = self.password_entry.get()
        self.password_2 = self.password2_entry.get()

        if self.user not in user_name:
            if self.user != '':
                if self.password != '' and self.password_2 != '':
                    if self.password == self.password_2:
                        user = {'user': self.user, 'password': self.password, 'level': 0}
                        with open(r'data\users.csv', 'w', newline='') as db:
                            fieldnames = ['user', 'password', 'level']
                            writer = csv.DictWriter(db, fieldnames=fieldnames)
                            writer.writeheader()
                            for row in self.controller.users:
                                writer.writerow(row)
                            writer.writerow(user)
                            db.close()
                            self.controller.user = self.user
                            self.controller.show_frame(SelectMode)
                    else:
                        messagebox.showwarning('Error', 'Contraseña no es igual')
            else:
                messagebox.showwarning('Error', 'Nombre vacío')
        else:
            messagebox.showwarning('Error', 'Usuarío repetido')


class Login:        
    
    def __init__(self, parent, controller):
    
        self.root = tk.Frame(parent)
        self.controller = controller

        user_label = tk.Label(self.root, text="Usuarío")
        user_label.grid(row=0, column=0)
        self.user_entry = tk.Entry(self.root, width=50)
        self.user_entry.grid(row=0, column=1)

        password_label = tk.Label(self.root, text="Contraseña")
        password_label.grid(row=1, column=0)
        self.password_entry = tk.Entry(self.root, width=50)
        self.password_entry.grid(row=1, column=1)

        sub_btn=tk.Button(self.root,text = 'Ingresar', command = self.login)
        sub_btn.grid(row=2, columnspan=2)

        back_btn=tk.Button(self.root,text = 'Regresar', command = self.back)
        back_btn.grid(row=3, columnspan=2)

    def back(self):
       
        self.controller.show_frame(Login_or_register)

    def login(self):
        
        users = []
        user_name = []
        user_password = []

        with open(r'data\users.csv', 'r') as db:
            csv_file = csv.DictReader(db)
            for row in csv_file:
                users.append(dict(row))
            self.controller.users = users
            db.close()

        for row in users:
            user_name.append(row['user'])
            user_password.append(row['password'])

        self.user = self.user_entry.get()
        self.password = self.password_entry.get()

        if self.user in user_name:
            if self.password == user_password[user_name.index(self.user)]:
                    self.controller.user = self.user
                    self.controller.show_frame(SelectMode)
            else:
                messagebox.showwarning('Error', 'Contraseña incorrecta')
        else:
            messagebox.showwarning('Error', 'Usuarío inexistente')



class SelectMode:
    
    def __init__(self, parent, controller):
    
        self.root = tk.Frame(parent)
        self.controller = controller

        user_label = tk.Label(
            self.root,
            text=f"Bienbenido {self.controller.user}",
            font=("Verdana", 20)
        )
        user_label.grid(row=0, column=0)

        game_mode = tk.Label(
            self.root,
            text="Elige el modo de juego:",
            font=("Arial", 14)
        )
        game_mode.grid(row=1, column=0)

        training_btn=tk.Button(self.root,text = 'Modo entrenamiento', command = self.mode1)
        training_btn.grid(row=2, column=0)
        
        history_btn=tk.Button(self.root,text = 'Modo historia', command = self.mode2)
        history_btn.grid(row=3, column=0)
        
        back_btn=tk.Button(self.root,text = 'Regresar', command = self.back)
        back_btn.grid(row=4, column=0)

    def mode1(self):
        self.controller.root.destroy()
        game.Game(self.controller.user, "mode1")
    
    def mode2(self):
        self.controller.root.destroy()
        game.Game(self.controller.user, "mode2")

    def back(self):
       
        self.controller.show_frame(Login_or_register)

if __name__ == "__main__":
    Start(Login_or_register)
