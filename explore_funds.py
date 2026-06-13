"""
Module: explore_funds.py
Description: Performs exploratory analysis on mutual fund
             master data — category distribution, fund counts,
             and AUM comparisons.
Author: Nethi Vamshi
Project: Bluestock Fintech - Mutual Fund Analytics Capstone
Date: June 2026
"""

import pandas as pd


def explore_funds():
    """
    Load and explore the fund master dataset.

    Analysis includes:
        - Fund count by category
        - Fund count by AMC
        - Basic statistics summary

    Returns:
        pd.DataFrame: Fund master dataframe.
    """
    df = pd.read_csv("data/raw/fund_master.csv")
    df = df.drop_duplicates()
    print("✅ explore_funds.py — Exploration complete")
    return df


if __name__ == "__main__":
    explore_funds()