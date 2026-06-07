import pandas as pd

df = pd.read_csv("data/raw/08_investor_transactions.csv")

# Remove duplicates
df = df.drop_duplicates()

# Amount should be positive
df = df[df["amount_inr"] > 0]

# Convert date
df["transaction_date"] = pd.to_datetime(df["transaction_date"])

df.to_csv("data/processed/08_investor_transactions_clean.csv", index=False)

print("Transactions cleaned")