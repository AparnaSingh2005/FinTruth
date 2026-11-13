
import pandas as pd
from src.features.financial_metrics import calculate_revenue_growth


def test_revenue_growth():

    data = pd.DataFrame({
        "ticker": ["ABC", "ABC"],
        "fiscal_year": [2023, 2024],
        "revenue": [100, 120]
    })

    result = calculate_revenue_growth(data)

    assert pd.isna(result.iloc[0]["revenue_growth"])

    assert round(
        result.iloc[1]["revenue_growth"], 2
    ) == 20.00
