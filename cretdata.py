import sqlite3
from sqlite3 import Error
def sql_connection():
    try:
        db1 = sqlite3.connect(':memory:')
        print("Connected")
    except Error:
        print(Error)
    finally:
        db1.close()
sql_connection()
