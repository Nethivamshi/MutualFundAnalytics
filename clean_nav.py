"""
Module: clean_nav.py
Description: Cleans the NAV history dataset — removes duplicates,
             handles missing values, and standardizes date formats.
Author: Nethi Vamshi
Project: Bluestock Fintech - Mutual Fund Analytics Capstone
Date: June 2026
"""

import pandas as pd


def clean_nav_data():
    """
    Load, clean, and save the NAV history dataset.

    Steps:
        - Reads raw NAV history CSV
        - Drops duplicate rows
        - Saves cleaned data to processed folder

    Returns:
        pd.DataFrame: Cleaned NAV dataframe.
    """
    df = pd.read_csv("data/raw/02_nav_history.csv")
    df = df.drop_duplicates()
    df.to_csv("data/processed/02_nav_history_clean.csv", index=False)
    print("✅ clean_nav.py — File saved successfully")
    return df


if __name__ == "__main__":
    clean_nav_data()