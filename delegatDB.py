
import sqlite3

conn = sqlite3.connect('efactura.db')
c = conn.cursor()
c.execute("""
            CREATE TABLE IF NOT EXISTS delegat (
                first_name TEXT,
                last_name TEXT,
                serie_buletin TEXT,
                nr_mijloc_transport TEXT
            )
        """)
conn.close()

def get_delegati():
    conn = sqlite3.connect('efactura.db')
    c = conn.cursor()
    c.execute(""" SELECT rowid, * FROM delegat """)
    rez = c.fetchall()
    conn.close()
    return rez

def add_delegat(om):
    conn = sqlite3.connect('efactura.db')
    c = conn.cursor()
    c.execute(""" INSERT INTO delegat VALUES ( ?, ?, ?, ? )  """, (om.first_name, om.last_name, om.serie_buletin, om.nr_mijloc_transport))
    conn.commit()
    conn.close()

def sterge_delegat(id):
    conn = sqlite3.connect('efactura.db')
    c = conn.cursor()
    c.execute(""" DELETE FROM delegat WHERE rowid = (?) """, (id,))
    conn.commit()
    conn.close()

def update_delegat(delegat, delegatId):
    conn = sqlite3.connect('efactura.db')
    c = conn.cursor()
    c.execute(""" UPDATE delegat SET first_name = ?, last_name = ?, serie_buletin = ?, nr_mijloc_transport = ?  WHERE rowid = ? """, (delegat.first_name, delegat.last_name, delegat.serie_buletin, delegat.nr_mijloc_transport, delegatId))
    conn.commit()
    conn.close()