import sqlite3

def create_db():
    conn = sqlite3.connect("supermarket.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        price REAL
    )
    """)

    # Insert sample products (only once)
    products = [
        ("Rice", 50),
        ("Milk", 25),
        ("Bread", 30),
        ("Sugar", 40)
    ]

    cursor.executemany("INSERT INTO products (name, price) VALUES (?, ?)", products)

    conn.commit()
    conn.close()

create_db()