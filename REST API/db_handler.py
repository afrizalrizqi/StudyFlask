#import library
import sqlite3 as sql

#Fungsi untuk melakukan connect ke dalam database
def connect_db():
    conn = sql.connect("company.db")
    return conn

#Fungsi untuk membuat database
def create_db():
    try:
        conn = connect_db()
        conn.execute('''
            CREATE TABLE employees(
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone TEXT NOT NULL,
                city TEXT NOT NULL
            );
        ''')
        conn.commit()
        print("Table employee berhasil dibuat")
    except:
        print("Ada error, table employee sudah ada")
    finally:
        conn.close()

# Running dari fungsi create database
create_db()