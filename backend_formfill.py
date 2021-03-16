import sqlite3


def connect():
    conn = sqlite3.connect("hotel.db")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS hotel (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, address TEXT, room TEXT, rent INTEGER)")
    conn.commit()
    conn.close()


def add_ent(name, age, address, room, rent):
    from backend_formfill import cal
    conn = sqlite3.connect("hotel.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO hotel VALUES (NULL,?,?,?,?,?)", (name, age, address, room, cal(room)))
    conn.commit()
    conn.close()
    view_ent()


def cal(room):
    if room == "normal" or "NORMAL":
        return 1300
    elif room == "deluxe" or "DELUXE":
        return 2000


def delete_ent(id):
    conn = sqlite3.connect("hotel.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM hotel WHERE id =?", (id,))
    conn.commit()
    conn.close()


def view_ent():
    conn = sqlite3.connect("hotel.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM hotel")
    rows = cur.fetchall()
    conn.close()
    return rows


def update_ent(id, name, age, address, room, rent):
    from backend_formfill import cal
    conn = sqlite3.connect("hotel.db")
    cur = conn.cursor()
    cur.execute("UPDATE hotel SET name=?, age=?, address=?, room=?, rent=? WHERE id=?",
                (name, age, address, room, cal(room), id))
    conn.commit()
    conn.close()

connect()