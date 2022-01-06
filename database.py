'''
This file uses SQLite to generate a database containing all of the Clepsh-Gordan Coefficients.
'''


import sqlite3
import pandas as pd

con = sqlite3.connect('CG.db')  # Connecting to the database
cur = con.cursor()  # Creating cursor object

# cur.execute('CREATE TABLE coefficients (j1 text, j2 text, m1 text, m2 text, J text, M text)')
# Columns: [j1, j2, m1, m2, J, M]
# cur.execute('ALTER TABLE coefficients ADD coefficient text;')

cur.execute("INSERT INTO coefficients (j1, j2, m1, m2, J, M, coefficient) \
            VALUES ('1/2', '1/2', '1/2', '1/2', 1, 1, 1); ")


cur.execute("INSERT INTO coefficients (j1, j2, m1, m2, J, M, coefficient) \
            VALUES ('1/2', '1/2', '1/2', '-1/2', 1, 0, '1/2');")
cur.execute("INSERT INTO coefficients (j1, j2, m1, m2, J, M, coefficient) \
            VALUES ('1/2', '1/2', '-1/2', '1/2', 1, 0, '1/2');") 
cur.execute("INSERT INTO coefficients (j1, j2, m1, m2, J, M, coefficient) \
            VALUES ('1/2', '1/2', '1/2', '-1/2', 0, 0, '1/2');")
cur.execute("INSERT INTO coefficients (j1, j2, m1, m2, J, M, coefficient) \
            VALUES ('1/2', '1/2', '-1/2', '1/2', 0, 0, '-1/2');")


cur.execute("INSERT INTO coefficients (j1, j2, m1, m2, J, M, coefficient) \
            VALUES ('1/2', '1/2', '-1/2', '-1/2', 1, -1, 1); ")

print(pd.read_sql_query("SELECT * FROM coefficients", con))
con.commit()
con.close()
