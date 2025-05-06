import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

class CalculatorDB:
    def __init__(self, db_name="calculator.db"):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.create_tables()

    def create_tables(self):
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            );
        """)
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                operation TEXT,
                a REAL,
                b REAL,
                result REAL,
                FOREIGN KEY(user_id) REFERENCES users(id)
            );
        """)
        self.conn.commit()  # ✅ Ensure table creation is committed

    # 🔐 USER AUTH
    def register_user(self, username, password):
        try:
            hashed_pw = generate_password_hash(password)
            self.conn.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (username, hashed_pw)
            )
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def validate_user(self, username, password):
        cursor = self.conn.execute(
            "SELECT id, password FROM users WHERE username = ?",
            (username,)
        )
        row = cursor.fetchone()
        if row and check_password_hash(row[1], password):
            return row[0]  # user_id
        return None

    # ⚙️ CALCULATOR OPERATIONS
    def calculate(self, user_id, op, a, b):
        if op == "add":
            res = a + b
        elif op == "subtract":
            res = a - b
        elif op == "multiply":
            res = a * b
        elif op == "divide":
            if b == 0:
                return "Error: Division by zero"
            res = a / b
        else:
            return "Invalid operation"
        
        self.conn.execute(
            "INSERT INTO history (user_id, operation, a, b, result) VALUES (?, ?, ?, ?, ?)",
            (user_id, op, a, b, res)
        )
        self.conn.commit()  # ✅ Ensure result is saved

        return res

    def read_all(self, user_id):
        cursor = self.conn.execute(
            "SELECT * FROM history WHERE user_id = ? ORDER BY id DESC",
            (user_id,)
        )
        return cursor.fetchall()

    def delete(self, record_id, user_id):
        self.conn.execute(
            "DELETE FROM history WHERE id = ? AND user_id = ?",
            (record_id, user_id)
        )
        self.conn.commit()

    def update(self, record_id, new_result, user_id):
        self.conn.execute(
            "UPDATE history SET result = ? WHERE id = ? AND user_id = ?",
            (new_result, record_id, user_id)
        )
        self.conn.commit()
