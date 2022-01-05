'''
This file uses SQLite to generate a database containing all of the Clepsh-Gordan Coefficients.
'''


import sqlite3


con = sqlite3.connect('CG.db')