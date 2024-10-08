import tkinter as tk

# Hàm để cập nhật biểu thức trong ô đầu vào
def btn_click(item):
    current = expression_field.get()
    expression_field.delete(0, tk.END)
    expression_field.insert(0, current + str(item))

# Hàm để xóa toàn bộ biểu thức
def btn_clear():
    expression_field.delete(0, tk.END)

# Hàm để tính toán và hiển thị kết quả
def btn_equal():
    try:
        result = str(eval(expression_field.get())) # Sử dụng eval để tính toán
        expression_field.delete(0, tk.END)
        expression_field.insert(0, result)
    except:
        expression_field.delete(0, tk.END)
        expression_field.insert(0, "Lỗi!")

# Tạo cửa sổ giao diện
win = tk.Tk()
win.title("Máy tính cơ bản")

# Tạo một ô để hiển thị biểu thức
expression_field = tk.Entry(win, width=30, borderwidth=5)
expression_field.grid(row=0, column=0, columnspan=4)

# Các nút cho máy tính
buttons = [
    '1', '2', '3', '/', 
    '4', '5', '6', '*', 
    '7', '8', '9', '-', 
    '0', 'C', '=', '+'
]

# Đặt các nút vào giao diện
row_value = 1
col_value = 0

for button in buttons:
    if button == "=":
        tk.Button(win, text=button, width=10, height=3, command=btn_equal).grid(row=row_value, column=col_value)
    elif button == "C":
        tk.Button(win, text=button, width=10, height=3, command=btn_clear).grid(row=row_value, column=col_value)
    else:
        tk.Button(win, text=button, width=10, height=3, command=lambda btn=button: btn_click(btn)).grid(row=row_value, column=col_value)

    col_value += 1
    if col_value > 3:
        col_value = 0
        row_value += 1

# Khởi động giao diện
win.mainloop()
