# Insert, Update, Delete, Select

import sqlite3

conn = sqlite3.connect("student.db")
cursor = conn.cursor()

# Insert
cursor.execute("INSERT INTO students VALUES (1, 'Ananya')")

# Update
cursor.execute("UPDATE students SET name='Riya' WHERE id=1")

# Select
cursor.execute("SELECT * FROM students")
print(cursor.fetchall())

# Delete
cursor.execute("DELETE FROM students WHERE id=1")

conn.commit()
conn.close()