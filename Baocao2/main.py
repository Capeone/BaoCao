import tkinter as tk
from model.user_model import UserModel
from view.user_view import UserView
from controller.user_controller import UserController
from config import db_config

# Khởi tạo ứng dụng
if __name__ == "__main__":
    root = tk.Tk()

    # Tạo các thành phần trong mô hình MVC
    model = UserModel(db_config)
    view = UserView(root)
    controller = UserController(model, view)

    root.mainloop()
