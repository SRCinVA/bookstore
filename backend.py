import sqlite3

# test functionality in the terminal first

def connect():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    conn.commit()
    conn.close()

def insert(title, author, year, isbn):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)", (title,author,year,isbn))  # NULL because python creates that ID automatically. Still need to add all parameters a second time as a tuple.
    conn.commit()                                                                       
    conn.close()

def view(): # fetches all rows
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book")
    # conn.commit() no need to commit any changes                                                                      
    rows=cur.fetchall()
    conn.close() 
    return rows

connect() # this ensures that this function will run when bookstore.py (and then backend.py) are run.
insert("The sea", "John Smith", 2021, 6565748746) 
print(view())
