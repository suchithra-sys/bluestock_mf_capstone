import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/02_nav_history.csv")

# Remove duplicates
df = df.drop_duplicates()

# Remove missing values
df = df.dropna()

# Save cleaned dataset
df.to_csv("data/processed/02_nav_history_clean.csv", index=False)

print("Data cleaned successfully")