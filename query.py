'''
query.py
This file contains a function which queries CG.db to get the coefficient values corresponding to those entered in interface.py 
'''
import sqlite3
import pandas as pd 


print("Connected")


def query(j1, j2, m1, m2, J, M):
    con = sqlite3.connect('CG.db')
    cur = con.cursor()
    query  = str(f"SELECT coefficient FROM coefficients WHERE j1= ? AND j2= ? AND m1= ? AND m2= ? AND J= ? AND M= ? ")
    params = (j1, j2, m1, m2, J, M)
    cur.execute(query, params)
    result = cur.fetchall()[0][0]
    cur.close()
    return result


query('1/2',"1/2", "-1/2", "1/2", 0, 0)

# print(pd.read_sql_query("SELECT * FROM coefficients", con))