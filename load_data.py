import pandas as pd
import sqlite3

conn = sqlite3.connect("bluestock_mf.db")

funds = pd.read_csv("data/raw/01_fund_master.csv")
nav = pd.read_csv("data/raw/02_nav_history.csv")

funds.to_sql("fund_master", conn, if_exists="replace", index=False)
nav.to_sql("nav_history", conn, if_exists="replace", index=False)

print("Data Loaded Successfully")

conn.close()