import tkinter as tk
from tkinter import messagebox

class LoginView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.frame = tk.Frame(self.root)
        self.setup_ui()

    def setup_ui(self):
        self.frame.pack(padx=10, pady=10)
        
        tk.Label(self.frame, text="Email:").grid(row=0, column=0, pady=5)
        self.email_entry = tk.Entry(self.frame)
        self.email_entry.grid(row=0, column=1, pady=5)
        
        tk.Label(self.frame, text="Senha:").grid(row=1, column=0, pady=5)
        self.password_entry = tk.Entry(self.frame, show="*")
        self.password_entry.grid(row=1, column=1, pady=5)
        
        tk.Button(self.frame, text="Login", command=self.handle_login).grid(row=2, column=0, columnspan=2, pady=10)

    def handle_login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        if self.controller.attempt_login(email, password):
            messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
            self.frame.destroy()
        else:
            messagebox.showerror("Erro", "Email ou senha inválidos.")

    def show(self):
        self.frame.pack()