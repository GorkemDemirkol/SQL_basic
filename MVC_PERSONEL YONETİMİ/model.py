import sqlite3

def db_connection():
    conn = sqlite3.connect('personel_veritabani.db')
    return conn
def create_table():
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS personel (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ad TEXT NOT NULL,
            soyad TEXT NOT NULL,
            yas INTEGER NOT NULL,
            departman TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()