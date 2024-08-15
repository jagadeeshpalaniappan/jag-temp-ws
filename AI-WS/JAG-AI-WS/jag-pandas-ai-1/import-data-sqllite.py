import sqlite3
import pandas as pd

con = sqlite3.connect('data.db')
wb = pd.read_excel('data.xlsx',sheet_name = None)

for sheet in wb:
    wb[sheet].to_sql(sheet,con,index=False)
con.commit()
con.close()