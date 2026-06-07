import pandas as pd

df = pd.read_csv("data/raw/02_nav_history.csv")

print("Original Shape:", df.shape)

print(df.columns)

df = df.drop_duplicates()

print("Cleaned Shape:", df.shape)

df.to_csv("data/processed/02_nav_history_clean.csv", index=False)

print("File saved successfully")