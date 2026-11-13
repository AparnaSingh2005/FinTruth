
import pandas as pd
from pathlib import Path

# Synthetic sample data for testing only
data = [
    {
        "company": "Alpha Technologies",
        "ticker": "SIMUS",
        "country": "US",
        "fiscal_year": 2023,
        "revenue": 100000000,
        "net_income": 20000000,
        "total_debt": 30000000,
        "total_assets": 150000000,
        "currency": "USD",
        "source_type": "synthetic",
        "data_status": "synthetic"
    },
    {
        "company": "Alpha Technologies",
        "ticker": "SIMUS",
        "country": "US",
        "fiscal_year": 2024,
        "revenue": 120000000,
        "net_income": 25000000,
        "total_debt": 28000000,
        "total_assets": 170000000,
        "currency": "USD",
        "source_type": "synthetic",
        "data_status": "synthetic"
    },
    {
        "company": "Beta Systems",
        "ticker": "SIMIN",
        "country": "India",
        "fiscal_year": 2023,
        "revenue": 5000000000,
        "net_income": 600000000,
        "total_debt": 1000000000,
        "total_assets": 8000000000,
        "currency": "INR",
        "source_type": "synthetic",
        "data_status": "synthetic"
    },
    {
        "company": "Beta Systems",
        "ticker": "SIMIN",
        "country": "India",
        "fiscal_year": 2024,
        "revenue": 5500000000,
        "net_income": 700000000,
        "total_debt": 900000000,
        "total_assets": 9000000000,
        "currency": "INR",
        "source_type": "synthetic",
        "data_status": "synthetic"
    }
]

df = pd.DataFrame(data)

output_path = Path("data/raw/sample_financials.csv")
output_path.parent.mkdir(parents=True, exist_ok=True)

df.to_csv(output_path, index=False)

print("FinTruth sample dataset created!")
print(df)
print(f"\nSaved to: {output_path}")
