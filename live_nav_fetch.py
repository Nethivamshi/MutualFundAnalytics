import pandas as pd
import requests
import os

base_dir = os.path.dirname(os.path.abspath(__file__))

url = "https://api.mfapi.in/mf/125497"

data = requests.get(url).json()

df = pd.DataFrame(data["data"])

save_path = os.path.join(base_dir, "data", "raw", "hdfc_nav.csv")

df.to_csv(save_path, index=False)

print("Saved Successfully")
print("Shape:", df.shape)
print(df.head())