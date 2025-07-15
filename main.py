import tkinter as tk
from view.splash_view import SplashView
from controller.auth_controller import AuthController

def main():
    root = tk.Tk()
    root.title("PyOnERP")
    root.geometry("400x300")
    
    def show_login():
        AuthController(root)
    
    SplashView(root, show_login)
    root.mainloop()

if __name__ == "__main__":
    main()