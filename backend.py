import sqlite3

# test functionality in the terminal first

class Database:
    # we need to create a "minimal object" when we call the class
    # we also had to give each attribute ('cur' and 'conn') an object, which was 'self.
    
    def __init__(self, db): # def __init__() is the "blueprint" of the object and a reserved function in Python that is called while no others are.
        self.conn=sqlite3.connect(db)  # init() takes care of this for all following methods
        self.cur=self.conn.cursor()         # init() takes care of this for all following methods
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
        self.conn.commit()
        # conn.close() don't need this for init.

    # these other functions are implemented when they are specifically called later
    def insert(self, title, author, year, isbn):
        self.cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)", (title,author,year,isbn))  # NULL because python creates that ID automatically. Still need to add all parameters a second time as a tuple.
        self.conn.commit()                                                                       
        self. conn.close()

    def view(self): # fetches all rows
        self.cur.execute("SELECT * FROM book")
        # conn.commit() no need to commit any changes                                                                      
        rows=self.cur.fetchall()
        self.conn.close() 
        return rows

    def search(self, title="", author="", year="", isbn=""):  # need to pass the id of the row to delete
        self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title,author,year,isbn)) #still unclear why you need to pass in this tuple
        rows=self.cur.fetchall()
        self.conn.close() 
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM book WHERE id=?", (id,)) # first is the "column name", then the "function parameter".
        # rows=cur.fetchall() won't need this one.
        self.conn.commit()
        self.conn.close()

    def update(self,id,title, author, year, isbn):
        self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id)) # column name" for id, then the "function parameter" for id.
        self.conn.commit()
        self.conn.close()

    # connect() def __init__() now takes care of this.

