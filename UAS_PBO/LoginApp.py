import tkinter as tk
from tkinter import messagebox

from . import RegisterApp as app_regis
from . import MenuApp as app_menu
from . import database as db 

class LoginApp:
    def __init__(self, root, username, password):
        self.root = root
        self.root.title("Login")
        self.username = username
        self.password = password
        bg_color = root.cget("bg")

        # Membuat frame dan menempatkannya di tengah jendela
        frame = tk.Frame(root, width=300, height=300, bg=bg_color)
        frame.place(relx=0.5, rely=0.4 , anchor=tk.CENTER)

        # Label "selamat datang"
        self.welcome_label = tk.Label(frame, text="Halo, selamat datang", font=("Futura", 14))
        self.welcome_label.grid(row=0, column=0, columnspan=2, pady=(50, 20))  # Padding atas diatur ke 50px

        # Label "Login"
        self.login_label = tk.Label(frame, text="Login", font=("Futura", 14))
        self.login_label.grid(row=1, column=0, columnspan=2, pady=20)

        # Label "username:"
        self.username_label = tk.Label(frame, text="Username: ", font=("Futura", 14))
        self.username_label.grid(row=2, column=0, pady=5, sticky='e')

        # Entry for username
        self.username_entry = tk.Entry(frame, width=30)
        self.username_entry.grid(row=2, column=1, pady=5)

        # Label "password:"
        self.password_label = tk.Label(frame, text="Password: ", font=("Futura", 14))
        self.password_label.grid(row=3, column=0, pady=5, sticky='e')

        # Entry for password
        self.password_entry = tk.Entry(frame, width=30)
        self.password_entry.grid(row=3, column=1, pady=5)

        # Button "Login"
        self.login_button = tk.Button(frame, text="Login", font=("Futura", 14), command=self.login)
        self.login_button.grid(row=4, column=0, columnspan=2, pady=10)

        # Button "Belum Punya Akun?"
        self.signup_button = tk.Button(frame, text="Belum Punya Akun?", font=("Futura", 14), command=self.register)
        self.signup_button.grid(row=5, column=0, columnspan=2, pady=10)

        # Button "keluar"
        self.exit_button = tk.Button(frame, text="keluar", font=("Futura", 14), command=self.exit_program)
        self.exit_button.grid(row=6, column=0, columnspan=2, pady=10)

    def login(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        
        db.query = f"select * from tbuser "
        db.cursor.execute(db.query)
        
        result = db.cursor.fetchall()
        
        for i in result:
            if i[1] == username and i[2] == password:
                messagebox.showinfo("login","Berhasil Login")
                self.root.destroy()
                app_menu.start()
                break
                
            else:
                messagebox.showinfo("login","Gagal Login")
        
        # if username == "a" and password == "a":
            
        # else:
            
    
    def register(self):
        self.root.destroy()
        app_regis.start()

    def exit_program(self):
        exit()

def start():
    root = tk.Tk()
    root.title("Login")
    root.attributes("-fullscreen", True)
    app = LoginApp(root, "", "")

    root.mainloop()

global root