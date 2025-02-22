# creating the database for user and books
import sqlite3 as sq

def connect_db():
    
    return sq.connect('library.db')

def table_setup():

    conn = connect_db()
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS books(
    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    status INTEGER DEFAULT 1)
    ''')
    c.execute('''
    CREATE TABLE IF NOT EXISTS user(
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    issued_books TEXT DEFAULT '')''')

    conn.commit()
    conn.close()
