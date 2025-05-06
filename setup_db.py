import sqlite3

conn = sqlite3.connect("calculator.db")
cursor = conn.cursor()

# DROP if exists
cursor.execute("DROP TABLE IF EXISTS history")

# Create table with user_id
cursor.execute("""
CREATE TABLE history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    operation TEXT NOT NULL,
    a REAL NOT NULL,
    b REAL NOT NULL,
    result REAL NOT NULL
)
""")

print("✅ Table 'history' created with user_id column.")
conn.commit()
conn.close()
