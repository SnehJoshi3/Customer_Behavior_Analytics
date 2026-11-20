import pandas as pd
import sqlite3

df = pd.read_csv('Customer_Behavior.csv')
conn = sqlite3.connect('Customer_Behavior.db')
df.to_sql('Customer_Behavior', conn, if_exists='replace', index=False)

conn.close()