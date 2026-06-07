import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///bluestock_mf.db")

nav = pd.read_csv("data/processed/02_nav_history_clean.csv")

nav.to_sql(
    "nav_history",
    engine,
    if_exists="replace",
    index=False
)

print("Database created")