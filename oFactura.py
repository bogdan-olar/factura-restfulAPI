import sqlite3

def numar_factura(numar):
    conn = sqlite3.connect('efactura.db')
    c = conn.cursor()

    c.execute("""
                SELECT * FROM factura WHERE numar = ?
                """, (numar,))
    fact = c.fetchone()
    conn.close()

    return fact

def get_one_client_after_id(id):
    conn = sqlite3.connect('efactura.db')
    c = conn.cursor()
    c.execute(""" SELECT rowid, * FROM client WHERE rowid = ? """, (id,))
    raspuns = c.fetchone()
    conn.close()
    return raspuns

def get_one_delegat_after_id(id):
    conn = sqlite3.connect('efactura.db')
    c = conn.cursor()
    c.execute(""" SELECT rowid, * FROM delegat WHERE rowid = ? """, (id,))
    raspuns = c.fetchone()
    conn.close()
    return raspuns

def get_bunuri_after_fact_number(number):
    conn = sqlite3.connect('efactura.db')
    c = conn.cursor()
    c.execute(""" SELECT rowid, * FROM bunuri_servicii WHERE numar_factura = ? """, (number,))
    raspuns = c.fetchall()
    conn.close()
    return raspuns