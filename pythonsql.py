
import sqlite3
import os

db_file = "gym_data.db"
athletes_data = [
    ("neo", 95, "quantum computing"),
    ("trinity", 110, "robotics"),
    ("morpheus", 75, "ai")
]

try:
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    print(f"db is connected. file: {os.path.abspath(db_file)}")
    
    # 🔥 FIX IS HERE: The SQL command must be a string passed to cursor.execute()
    cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS athletes(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            bench_press_kg INTEGER,
            favorite_tech TEXT
        )
    """)
    print("tabel schema confirmed")

    # The rest of your script (inserting/fetching) should follow here
    # Example:
    # insert_query = "INSERT INTO athletes (name, bench_press_kg, favorite_tech) VALUES (?, ?, ?)"
    # cursor.executemany(insert_query, athletes_data)
    # conn.commit()
    
except sqlite3.Error as e:
    print(f"SQLite Error encountered: {e}")
    
finally:
    if 'conn' in locals() and conn: # Ensure conn exists before closing
        conn.close()