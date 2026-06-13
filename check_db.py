"""
Module: check_db.py
Description: Verifies the SQLite database tables created
             for the Mutual Fund Analytics project.
Author: Nethi Vamshi
Project: Bluestock Fintech - Mutual Fund Analytics Capstone
Date: June 2026
"""

import sqlite3


def check_tables():
    """
    Connect to bluestock_mf.db and return all table names.

    Returns:
        list: List of table names in the database.
    """
    conn = sqlite3.connect("bluestock_mf.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    conn.close()
    return tables


if __name__ == "__main__":
    tables = check_tables()
    print(f"Tables in database: {tables}")