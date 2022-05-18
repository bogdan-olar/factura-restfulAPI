
import sqlite3

conn = sqlite3.connect('efactura.db')
c = conn.cursor()
c.execute("""
                CREATE TABLE IF NOT EXISTS emitent (
                    nume_societate TEXT,
                    tip_societate TEXT,
                    reg_com TEXT,
                    cod_fiscal TEXT,
                    cod_tva TEXT,
                    capital_social TEXT,
                    localitate TEXT,
                    strada TEXT,
                    numar TEXT,
                    scara TEXT,
                    apartament TEXT,
                    judet TEXT,
                    telefon TEXT,
                    email TEXT,
                    contIBAN TEXT,
                    denumireBanca TEXT
                 )
            """)
conn.close()

# conn = sqlite3.connect('efactura.db')
# c = conn.cursor()
# c.execute(""" 
#                  INSERT INTO emitent VALUES ( 'Trident', 'SRL', 'J32/34/1999', '344556', 'RO', '200', 'Sibiu', 'Milea', '12', 'B', '1', 'Sibiu', '0729876322', 'tr@gmail.com', 'RO12TREZ564738882EUR', 'Transilvania' )
#          """)
# conn.commit()
# conn.close()



def get_emitent():
    conn = sqlite3.connect('efactura.db')
    c = conn.cursor()
    c.execute(""" SELECT rowid, * FROM emitent WHERE rowid = 1 """)
    rez = c.fetchone()
    conn.close()
    return rez

def update_emitent(emi):
    conn = sqlite3.connect('efactura.db')
    c = conn.cursor()
    c.execute(""" 
                 UPDATE emitent SET
                    nume_societate = ?,
                    tip_societate = ?,
                    reg_com = ?,
                    cod_fiscal = ?,
                    cod_tva = ?,
                    capital_social = ?,
                    localitate = ?,
                    strada = ?,
                    numar = ?,
                    scara = ?,
                    apartament = ?,
                    judet = ?,
                    telefon = ?,
                    email = ?,
                    contIBAN = ?,
                    denumireBanca = ?
                    WHERE rowid = 1
              """, (emi.numeSocietate, emi.tipSocietate, emi.regCom, emi.codFiscal, emi.codTva, emi.capitalSocial, emi.localitate, emi.strada, emi.numar, emi.scara, emi.apartament, emi.judet, emi.telefon, emi.email, emi.contIBAN, emi.denumireBanca))
    conn.commit()
    conn.close()