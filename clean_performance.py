import pandas as pd

df = pd.read_csv("data/raw/07_scheme_performance.csv")

df = df.drop_duplicates()

df.to_csv("data/processed/07_scheme_performance_clean.csv", index=False)

print("Performance data cleaned")