
import sqlite3

conn = sqlite3.connect('efactura.db')
c = conn.cursor()
c.execute("""
            CREATE TABLE IF NOT EXISTS client(
                nume_societate TEXT,
                tip_societate TEXT,
                reg_com TEXT,
                cod_fiscal TEXT,
                cod_tva TEXT,
                telefon TEXT,
                email TEXT
            )
         """)
conn.close()

def get_clienti():
    conn = sqlite3.connect('efactura.db')
    c = conn.cursor()
    c.execute(""" SELECT rowid, * FROM client """)
    r = c.fetchall()
    conn.close()
    return r

def get_one_client(nume):
    conn = sqlite3.connect('efactura.db')
    c = conn.cursor()
    c.execute(""" SELECT rowid, * FROM client WHERE nume_societate = ?""", (nume,))
    rs = c.fetchone()
    conn.close()
    return rs

def add_client(firma):
    conn = sqlite3.connect('efactura.db')
    c = conn.cursor()
    c.execute(""" INSERT INTO client VALUES ( ?, ?, ?, ?, ?, ?, ? ) """,
    (firma.numeClient, firma.tipClient, firma.regCom, firma.codFiscal, firma.codTva, firma.telefon, firma.email) )
    conn.commit()
    conn.close()

def delete_client(id):
    conn = sqlite3.connect('efactura.db')
    c = conn.cursor()
    c.execute(""" DELETE FROM client WHERE rowid = ? """, (id,))
    conn.commit()
    conn.close()

def update_client(cl):
    conn = sqlite3.connect('efactura.db')
    c = conn.cursor()
    c.execute(""" UPDATE client SET nume_societate = ?, tip_societate = ?, reg_com = ?, cod_fiscal = ?, cod_tva = ?, telefon = ?, email = ? WHERE rowid = ? """,(cl['numeClient'], cl['tipClient'], cl['regCom'], cl['codFiscal'], cl['codTva'], cl['telefon'], cl['email'], cl['id']))
    conn.commit()
    conn.close()