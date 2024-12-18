from tkinter import messagebox


class UserController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        # Gắn sự kiện cho các nút
        self.view.button_login.config(command=self.login)
        self.view.button_register.config(command=self.register)

    def login(self):
        username = self.view.entry_username.get()
        password = self.view.entry_password.get()

        if not username or not password:
            messagebox.showwarning("Input Error", "Username and Password cannot be empty!")
            return

        result = self.model.check_login(username, password)
        if result:
            messagebox.showinfo("Success", "Login successful!")
            data = self.model.fetch_data()
            self.view.show_data_window(data)
        else:
            messagebox.showwarning("Failed", "Invalid username or password!")

    def register(self):
        username = self.view.entry_username.get()
        password = self.view.entry_password.get()

        if not username or not password:
            messagebox.showwarning("Input Error", "Username and Password cannot be empty!")
            return

        success = self.model.register_user(username, password)
        if success:
            messagebox.showinfo("Success", "Registration successful!")
        else:
            messagebox.showwarning("Error", "Username already exists!")
