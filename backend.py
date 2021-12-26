import sqlite3

# test functionality in the terminal first

def connect():
    conn=sqlite.connect("books.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    conn.commit()
    conn.close()

connect() # this ensures that this function will run when bookstore.py (and then backend.py) are run.

