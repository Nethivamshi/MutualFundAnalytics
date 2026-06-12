import pandas as pd

scorecard = pd.read_csv("data/processed/fund_scorecard.csv")

risk = input("Enter risk appetite Low / Moderate / High: ")

if risk == "Low":
    result = scorecard[scorecard["risk_category"] == "Low"].head(3)
elif risk == "Moderate":
    result = scorecard[scorecard["risk_category"] == "Moderate"].head(3)
else:
    result = scorecard[scorecard["risk_category"] == "High"].head(3)

print(result[["scheme_name", "fund_score", "sharpe_ratio"]])