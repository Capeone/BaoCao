import psycopg2

class UserModel:
    def __init__(self, db_config):
        self.db_config = db_config

    def connect(self):
        return psycopg2.connect(**self.db_config)

    def check_login(self, username, password):
        conn = self.connect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        result = cur.fetchone()
        cur.close()
        conn.close()
        return result

    def register_user(self, username, password):
        conn = self.connect()
        cur = conn.cursor()

        # Kiểm tra người dùng đã tồn tại chưa
        cur.execute("SELECT * FROM users WHERE username = %s", (username,))
        result = cur.fetchone()

        if result:
            cur.close()
            conn.close()
            return False

        # Thêm người dùng mới
        cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        conn.commit()
        cur.close()
        conn.close()
        return True

    def fetch_data(self):
        conn = self.connect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users")
        data = cur.fetchall()
        cur.close()
        conn.close()
        return data
