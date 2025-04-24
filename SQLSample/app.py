from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app=Flask(__name__)

#database bağla
def db_connect():

    conn=sqlite3.connect('kullanici_database.db')
    return conn
#ana sayfa
@app.route('/')
def index():
    conn=db_connect()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM kullanicilar")
    kullanicilar=cursor.fetchall()
    conn.close()
    return render_template('index.html', kullanicilar=kullanicilar)
#kayıt ekle
@app.route('/add',methods=['POST'])
def add_record():
    isim=request.form['isim']
    yas=request.form['yas']
    if isim and yas:
        conn=db_connect()
        cursor=conn.cursor()
        cursor.execute("INSERT INTO kullanicilar (isim, yas) VALUES (?, ?)", (isim, yas))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
@app.route('/delete/<int:id>', methods= ['POST'])
def delete_record(id):
    conn=db_connect()
    cursor=conn.cursor()
    cursor.execute('DELETE FROM kullanicilar WHERE id=?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))
@app.route('/update/<int:id>', methods= ['POST'])
def update_record(id):
    yeni_isim=request.form['isim']
    Yeni_yas=request.form['yas']
    conn=db_connect()
    cursor=conn.cursor()
    cursor.execute('UPDATE kullanicilar SET isim=?, yas=? WHERE id=?', (yeni_isim, Yeni_yas, id))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))
#tablo oluştur
def create_table():
    conn=db_connect()
    cursor=conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS kullanicilar(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    isim TEXT NOT NULL,
                    yas INTEGER NOT NULL)''')
    conn.commit()
    conn.close()

if __name__=='__main__':
    create_table()
    app.run(debug=True)