
import pandas as pd


def calculate_revenue_growth(df: pd.DataFrame) -> pd.DataFrame:

    df = df.sort_values(
        ["ticker", "fiscal_year"]
    ).copy()

    df["revenue_growth"] = (
        df.groupby("ticker")["revenue"]
        .pct_change() * 100
    )

    return df


if __name__ == "__main__":

    data = pd.read_csv("data/raw/sample_financials.csv")

    result = calculate_revenue_growth(data)

    print(
        result[
            ["company", "fiscal_year", "revenue_growth"]
        ]
    )
