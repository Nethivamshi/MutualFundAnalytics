"""
Module: load_data.py
Description: Loads all raw mutual fund CSV datasets into
             the SQLite database (bluestock_mf.db) using
             pandas and sqlite3.
Author: Nethi Vamshi
Project: Bluestock Fintech - Mutual Fund Analytics Capstone
Date: June 2026
"""

import pandas as pd
import sqlite3


def load_data():
    """
    Load all mutual fund CSV files into SQLite database.

    Datasets loaded:
        - 01_fund_master.csv     → fund_master table
        - 02_nav_history.csv     → nav_history table

    Returns:
        None
    """
    conn = sqlite3.connect("bluestock_mf.db")

    funds = pd.read_csv("data/raw/01_fund_master.csv")
    nav   = pd.read_csv("data/raw/02_nav_history.csv")

    funds.to_sql("fund_master", conn,
                 if_exists="replace", index=False)
    nav.to_sql("nav_history",   conn,
               if_exists="replace", index=False)

    conn.close()
    print("✅ load_data.py — Data Loaded Successfully")


if __name__ == "__main__":
    load_data()