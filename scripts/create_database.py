import sqlite3

conn = sqlite3.connect("sql/bluestock_mf.db")

print("Database created successfully")

conn.close()