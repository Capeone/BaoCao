from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Cấu hình kết nối cơ sở dữ liệu SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Định nghĩa mô hình Student để quản lý bảng sinh viên
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    IDS = db.Column(db.String(20), nullable=False, unique=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    major = db.Column(db.String(100), nullable=False)


# Tạo bảng trong cơ sở dữ liệu
with app.app_context():
    db.create_all()

# Trang chủ hiển thị danh sách sinh viên
@app.route('/')
def index():
    students = Student.query.all()
    return render_template('index.html', students=students)

# Route thêm sinh viên
@app.route('/add', methods=['POST'])
def add_student():
    name = request.form.get('name')
    IDS = request.form.get('IDS')
    age = request.form.get('age')
    major = request.form.get('major')
    
    # Tạo sinh viên mới và thêm vào cơ sở dữ liệu
    new_student = Student(name=name, IDS=str(IDS), age=int(age), major=major)
    db.session.add(new_student)
    db.session.commit()
    
    return redirect(url_for('index'))

# Route xóa sinh viên
@app.route('/delete/<int:student_id>')
def delete_student(student_id):
    student = Student.query.get(student_id)
    if student:
        db.session.delete(student)
        db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
