
import sqlite3

conn = sqlite3.connect('eFacturaUser.db')
c = conn.cursor()
c.execute("""
             CREATE TABLE IF NOT EXISTS user (
                 user_name TEXT,
                 email TEXT,
                 functia TEXT,
                 parola TEXT
             )
          """)
conn.close()

def add_user(om):
    conn = sqlite3.connect('eFacturaUser.db')
    c = conn.cursor()
    c.execute("""
                INSERT INTO user VALUES ( ?, ?, ?, ? )
              """, (om.user_name, om.email, om.functia, om.parola))
    conn.commit()
    conn.close()

def select_all():
    conn = sqlite3.connect('eFacturaUser.db')
    c = conn.cursor()
    c.execute(""" SELECT * FROM user """)
    response = c.fetchall()
    conn.close()
    return response