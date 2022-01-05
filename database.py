'''
This file uses SQLite to generate a database containing all of the Clepsh-Gordan Coefficients.
'''


import sqlite3
import pandas as pd

con = sqlite3.connect('CG.db')  # Connecting to the database
cur = con.cursor()  # Creating cursor object

# cur.execute('CREATE TABLE coefficients (j1 text, j2 text, m1 text, m2 text, J text, M text)')

print(pd.read_sql_query("SELECT * FROM coefficients", con))
