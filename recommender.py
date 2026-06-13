"""
Module: recommender.py
Description: Simple rule-based mutual fund recommender system.
             Suggests suitable funds based on investor risk
             appetite (Low / Moderate / High) using fund
             scorecard rankings.
Author: Nethi Vamshi
Project: Bluestock Fintech - Mutual Fund Analytics Capstone
Date: June 2026
"""

import pandas as pd


def recommend_funds(risk_appetite):
    """
    Recommend top 3 mutual funds based on investor risk appetite.

    Args:
        risk_appetite (str): Risk level — 'Low', 'Moderate',
                             or 'High'.

    Returns:
        pd.DataFrame: Top 3 recommended funds with scheme name,
                      fund score, and Sharpe ratio.
    """
    scorecard = pd.read_csv("data/processed/fund_scorecard.csv")

    result = scorecard[
        scorecard["risk_category"] == risk_appetite
    ].head(3)

    return result[["scheme_name", "fund_score", "sharpe_ratio"]]


if __name__ == "__main__":
    risk = input("Enter risk appetite Low / Moderate / High: ")
    recommendations = recommend_funds(risk)
    print("\n Recommended Funds:")
    print(recommendations)