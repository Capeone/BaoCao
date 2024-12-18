import tkinter as tk
from tkinter import ttk, messagebox

class UserView:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")

        # Giao diện đăng nhập
        self.label_username = tk.Label(root, text="Username:")
        self.label_username.pack(pady=5)

        self.entry_username = tk.Entry(root)
        self.entry_username.pack(pady=5)

        self.label_password = tk.Label(root, text="Password:")
        self.label_password.pack(pady=5)

        self.entry_password = tk.Entry(root, show="*")
        self.entry_password.pack(pady=5)

        self.button_login = tk.Button(root, text="Login")
        self.button_login.pack(pady=10)

        self.button_register = tk.Button(root, text="Register")
        self.button_register.pack(pady=10)

        # Cửa sổ hiển thị dữ liệu
        self.data_window = None

    def show_data_window(self, data):
        if self.data_window is None or not self.data_window.winfo_exists():
            self.data_window = tk.Toplevel(self.root)
            self.data_window.title("User Data")

            self.tree = ttk.Treeview(self.data_window, columns=("ID", "Username", "Password"), show="headings")
            self.tree.heading("ID", text="ID")
            self.tree.heading("Username", text="Username")
            self.tree.heading("Password", text="Password")
            self.tree.pack(fill="both", expand=True)

            # Hiển thị dữ liệu
            for row in data:
                self.tree.insert("", "end", values=row)
