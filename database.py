import sqlite3

def connect():
    conn=sqlite3.connect("block_list.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS block_list (id INTEGER PRIMARY KEY, url text)")
    conn.commit()
    conn.close()

def insert(url):
    conn=sqlite3.connect("block_list.db")
    cur=conn.cursor()
    print(url)
    #question mark is basically equal to {}.format()
    cur.execute("INSERT INTO block_list VALUES (NULL, ?)",(url,))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("block_list.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM block_list")
    rows=cur.fetchall()
    conn.close()
    return(rows)

def search(url=""):
    conn=sqlite3.connect("block_list.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM block_list WHERE url=?",(url,))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("block_list.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM block_list WHERE id={}".format(id))
    conn.commit()
    conn.close()

def update(id, url):
    conn=sqlite3.connect("block_list.db")
    cur=conn.cursor()
    cur.execute("UPDATE block_list SET url=? WHERE id=?",(url, id))
    conn.commit()
    conn.close()  

