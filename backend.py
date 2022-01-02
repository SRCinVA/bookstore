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

def search(title="", author="", year="", isbn=""):  # need to pass the id of the row to delete
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title,author,year,isbn)) #still unclear why you need to pass in this tuple
    rows=cur.fetchall()
    conn.close() 
    return rows

def delete(id,title,author,year,isbn):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?", (id,title,author,year,isbn)) # first is the "column name", then the "function parameter".
    # rows=cur.fetchall() won't need this one.
    conn.commit()
    conn.close()

def update(id,title, author, year, isbn):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id)) # column name" for id, then the "function parameter" for id.
    conn.commit()
    conn.close()

connect() # this ensures that this function will run when bookstore.py (and then backend.py) are run.
# insert("A Great Work of Art", "Yours Truly", 2100, 5464758696)
print(view())  # view all existing records
