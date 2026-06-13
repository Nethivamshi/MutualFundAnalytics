"""
Module: create_database.py
Description: Creates the SQLite database schema and all tables
             for the Mutual Fund Analytics project.
Author: Nethi Vamshi
Project: Bluestock Fintech - Mutual Fund Analytics Capstone
Date: June 2026
"""

import sqlite3


def create_database():
    """
    Create SQLite database and define all required tables.

    Tables created:
        - nav_history
        - fund_master
        - investor_transactions
        - scheme_performance
        - portfolio_holdings

    Returns:
        None
    """
    conn = sqlite3.connect("bluestock_mf.db")
    cursor = conn.cursor()

    with open("schema.sql", "r") as f:
        schema = f.read()

    cursor.executescript(schema)
    conn.commit()
    conn.close()
    print("✅ create_database.py — Database created successfully")


if __name__ == "__main__":
    create_database()