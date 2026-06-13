"""
Module: data_ingestion.py
Description: Loads all raw mutual fund CSV datasets into
             the SQLite database using SQLAlchemy.
Author: Nethi Vamshi
Project: Bluestock Fintech - Mutual Fund Analytics Capstone
Date: June 2026
"""

import pandas as pd
import sqlite3
import os


def ingest_all_data():
    """
    Load all cleaned CSV files into the SQLite database.

    Reads from:
        data/processed/ folder

    Loads into:
        bluestock_mf.db SQLite database

    Returns:
        None
    """
    conn = sqlite3.connect("bluestock_mf.db")

    csv_table_map = {
        "data/processed/02_nav_history_clean.csv":          "nav_history",
        "data/processed/investor_transactions_clean.csv":   "investor_transactions",
        "data/processed/scheme_performance_clean.csv":      "scheme_performance",
    }

    for csv_path, table_name in csv_table_map.items():
        if os.path.exists(csv_path):
            df = pd.read_csv(csv_path)
            df.to_sql(table_name, conn,
                      if_exists="replace", index=False)
            print(f"✅ Loaded {table_name}")
        else:
            print(f"⚠️  File not found: {csv_path}")

    conn.close()
    print("✅ data_ingestion.py — All data loaded successfully")


if __name__ == "__main__":
    ingest_all_data()