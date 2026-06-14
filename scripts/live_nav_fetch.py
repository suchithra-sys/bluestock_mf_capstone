import requests
import pandas as pd

url = "https://api.mfapi.in/mf/125497"

response = requests.get(url)

data = response.json()

# Convert NAV data to dataframe
df = pd.DataFrame(data['data'])

# Save CSV
df.to_csv("data/raw/live_nav.csv", index=False)

print("Live NAV Data Saved Successfully")

print(df.head())