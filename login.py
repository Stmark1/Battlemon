import tkinter as tk


class Start:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("400x400")
        self.root.title("Fightcreatures")
        self.root.resizable(width=False, height=False)

        container = tk.Frame(self.root) 
        container.pack(side = "top", fill = "both", expand = True)
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        
        self.frames = {}

        for frame in (Login_or_register, Register, Login):
            page = frame(container, self)
            self.frames[frame] = page
  
            page.root.grid(row = 0, column = 0, sticky ="nsew")
        
        self.show_frame(Login_or_register)

        self.root.mainloop()

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.root.tkraise()

    


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
        user_entry = tk.Entry(self.root, width=50)
        user_entry.grid(row=0, column=1)

        password_label = tk.Label(self.root, text="Contraseña")
        password_label.grid(row=1, column=0)
        password_entry = tk.Entry(self.root, width=50)
        password_entry.grid(row=1, column=1)

        password2_label = tk.Label(self.root, text="Repita la contraseña")
        password2_label.grid(row=2, column=0)
        password2_entry = tk.Entry(self.root, width=50)
        password2_entry.grid(row=2, column=1)

        user = user_entry.get()
        password = password_entry.get()

class Login:        
    def __init__(self, parent, controller):
        self.root = tk.Frame(parent)
        self.controller = controller

        user_label = tk.Label(self.root, text="Usuarío")
        user_label.grid(row=0, column=0)
        user_entry = tk.Entry(self.root, width=50)
        user_entry.grid(row=0, column=1)

        password_label = tk.Label(self.root, text="Contraseña")
        password_label.grid(row=1, column=0)
        password_entry = tk.Entry(self.root, width=50)
        password_entry.grid(row=1, column=1)

        user = user_entry.get()
        password = password_entry.get()


if __name__ == "__main__":
    Start()
