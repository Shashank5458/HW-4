import sqlite3
from sqlite3 import Error
def sql_connection():
    try:
        db1 = sqlite3.connect('mydatabase.db')
        return db1
    except Error:
        print(Error)
def sql_table(db1):
    sql3obj = db1.cursor()
    sql3obj.execute("CREATE TABLE student( id INTEGER PRIMARY KEY,cname TEXT,email TEXT,phone TEXT,address TEXT)")
    db1.commit()
db1 = sql_connection()
sql_table(db1)
