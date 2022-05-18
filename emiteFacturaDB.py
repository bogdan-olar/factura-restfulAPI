import sqlite3

conn = sqlite3.connect('efactura.db')
c = conn.cursor()
c.execute("""
            CREATE TABLE IF NOT EXISTS factura (
                serie TEXT,
                numar INTEGER,
                data TEXT,
                client_id INTEGER,
                delegat_id INTEGER
            )
          """)
conn.close()

conn = sqlite3.connect('efactura.db')
c = conn.cursor()
c.execute("""
            CREATE TABLE IF NOT EXISTS bunuri_servicii (
                denumire TEXT,
                cantitate REAL,
                fel TEXT,
                pret_bucata REAL,
                cota_tva INTEGER,
                numar_factura INTEGER
            )
          """)
conn.close()

def get_facturi():
    conn = sqlite3.connect('efactura.db')
    c = conn.cursor()
    c.execute("""
                SELECT factura.rowid, factura.serie, factura.numar, factura.data, client.nume_societate, client.tip_societate, client.reg_com, client.cod_fiscal, client.cod_tva, client.telefon, client.email FROM factura INNER JOIN client ON factura.client_id = client.rowid
              """) 
    r = c.fetchall()
    conn.close()
    return r

def add_factura( factura ):
    conn = sqlite3.connect('efactura.db')
    c = conn.cursor()
    c.execute("""
                INSERT INTO factura VALUES ( ?, ?, ?, ?, ? )
              """, (factura.serie, factura.numar, factura.data, factura.client_id, factura.delegat_id) )
    conn.commit()
    conn.close()

def add_bunuri( bS ):
    conn = sqlite3.connect('efactura.db')
    c = conn.cursor()
    c.execute("""
                INSERT INTO bunuri_servicii VALUES ( ?, ?, ?, ?, ?, ? )
              """, ( bS.denumire, bS.cantitate, bS.fel, bS.pret_bucata, bS.cota_tva, bS.numar_factura ))
    conn.commit()
    conn.close()