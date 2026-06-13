"""
Module: clean_transactions.py
Description: Cleans the investor transactions dataset — removes
             duplicates and validates transaction values.
Author: Nethi Vamshi
Project: Bluestock Fintech - Mutual Fund Analytics Capstone
Date: June 2026
"""

import pandas as pd


def clean_transactions():
    """
    Load, clean, and save the investor transactions dataset.

    Steps:
        - Reads raw transactions CSV
        - Drops duplicate rows
        - Removes rows with null transaction amounts
        - Saves cleaned data to processed folder

    Returns:
        pd.DataFrame: Cleaned transactions dataframe.
    """
    df = pd.read_csv("data/raw/investor_transactions.csv")
    df = df.drop_duplicates()
    df = df.dropna(subset=['amount'])
    df.to_csv("data/processed/investor_transactions_clean.csv", index=False)
    print("✅ clean_transactions.py — File saved successfully")
    return df


if __name__ == "__main__":
    clean_transactions()