import pandas as pd
import os

# This makes the path always relative to the script's location
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "data", "raw", "01_fund_master.csv")

df = pd.read_csv(file_path)

print("Missing Values")
print(df.isnull().sum())

print("\nDuplicates")
print(df.duplicated().sum())