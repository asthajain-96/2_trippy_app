'''
This is the backend script for the bookstore program
'''
import sqlite3
from tkinter import messagebox
# define a connection to a database
def connect():
    conn= sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("CREATe TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()

def insert(title, author, year, isbn):
    conn= sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book values (NULL,?,?,?,?)", (title, author, year, isbn))
    conn.commit()
    conn.close()

def view():
    conn= sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(title="", author="", year="", isbn=""):
    conn=sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",(title, author, year, isbn))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn= sqlite3.connect("books.db")
    cur = conn.cursor()
    # check if really want to delete:
    confirm = messagebox.askyesno('Delete Item','Are you sure you want to delete this?')
    if confirm:
        cur.execute("DELETE FROM book WHERE id=? ", (id,))
        conn.commit()
    conn.close()

def update(id,title, author, year, isbn):
    conn= sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title=?, author =?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
    conn.commit()
    conn.close()

connect()
#insert("The Earth", "John Smit", 1768, 898772873)
#delete(3)
'''
print(search(author="Dan Brown"))
print(view())
'''
