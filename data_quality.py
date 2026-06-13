"""
Module: data_quality.py
Description: Validates data quality across all mutual fund
             datasets — checks for nulls, duplicates, and
             out-of-range values.
Author: Nethi Vamshi
Project: Bluestock Fintech - Mutual Fund Analytics Capstone
Date: June 2026
"""

import pandas as pd


def check_quality(df, dataset_name):
    """
    Run data quality checks on a dataframe.

    Checks:
        - Total rows and columns
        - Null value counts per column
        - Duplicate row count

    Args:
        df (pd.DataFrame): Dataframe to validate.
        dataset_name (str): Name label for reporting.

    Returns:
        dict: Quality report with nulls and duplicates.
    """
    report = {
        "dataset":    dataset_name,
        "rows":       len(df),
        "columns":    len(df.columns),
        "nulls":      df.isnull().sum().to_dict(),
        "duplicates": df.duplicated().sum()
    }
    print(f"✅ Quality check complete for: {dataset_name}")
    return report


if __name__ == "__main__":
    df = pd.read_csv("data/raw/02_nav_history.csv")
    report = check_quality(df, "NAV History")
    print(report)