"""
Module: clean_performance.py
Description: Cleans the scheme performance dataset — handles
             missing values and standardizes column formats.
Author: Nethi Vamshi
Project: Bluestock Fintech - Mutual Fund Analytics Capstone
Date: June 2026
"""

import pandas as pd


def clean_performance():
    """
    Load, clean, and save the scheme performance dataset.

    Steps:
        - Reads raw scheme performance CSV
        - Drops duplicate rows
        - Fills missing numeric values with 0
        - Saves cleaned data to processed folder

    Returns:
        pd.DataFrame: Cleaned performance dataframe.
    """
    df = pd.read_csv("data/raw/scheme_performance.csv")
    df = df.drop_duplicates()
    df = df.fillna(0)
    df.to_csv("data/processed/scheme_performance_clean.csv", index=False)
    print("✅ clean_performance.py — File saved successfully")
    return df


if __name__ == "__main__":
    clean_performance()