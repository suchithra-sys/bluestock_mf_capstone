import pandas as pd

performance = pd.read_csv(
    r"C:\Users\suchithra\Downloads\MutualFundProject\data\raw\07_scheme_performance.csv"
)

risk = input("Risk Level (Low/Moderate/High): ")

top_funds = performance.sort_values(
    "sharpe_ratio",
    ascending=False
).head(3)

print(
    top_funds[
        [
            "scheme_name",
            "sharpe_ratio"
        ]
    ]
)