import pandas as pd
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "data", "raw", "01_fund_master.csv")

df = pd.read_csv(file_path)

print("Fund Houses:")
print(df["fund_house"].unique())

print("\nCategories:")
print(df["category"].unique())

print("\nRisk Grades:")
print(df["risk_category"].unique())