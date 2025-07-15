import tkinter as tk
from tkinter import ttk
import time

class SplashView:
    def __init__(self, root, callback):
        self.root = root
        self.callback = callback
        self.frame = tk.Frame(self.root)
        self.frame.pack(fill="both", expand=True)
        self.setup_ui()

    def setup_ui(self):
        tk.Label(self.frame, text="Bem-vindo ao PyOnERP", font=("Arial", 16)).pack(pady=20)
        self.progress = ttk.Progressbar(self.frame, length=200, mode='determinate')
        self.progress.pack(pady=10)
        self.root.after(100, self.update_progress)

    def update_progress(self):
        for i in range(101):
            self.progress['value'] = i
            self.root.update()
            time.sleep(0.03)
        self.frame.destroy()
        self.callback()