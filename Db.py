import sqlite3

conn = sqlite3.connect("company.db")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS employees")
cur.execute("""
CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary INTEGER,
    city TEXT
)
""")

data = [
    (1, 'Priya', 'IT', 60000, 'Coimbatore'),
    (2, 'Ravi', 'HR', 45000, 'Chennai'),
    (3, 'Anitha', 'IT', 75000, 'Coimbatore'),
    (4, 'Kumar', 'Sales', 50000, 'Madurai'),
    (5, 'Divya', 'HR', 55000, 'Chennai'),
    (6, 'Suresh', 'IT', 80000, 'Bangalore')
]

cur.executemany("INSERT INTO employees VALUES (?,?,?,?,?)", data)
conn.commit()
conn.close()
print("DB Ready!")