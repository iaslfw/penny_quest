import pandas as pd
from src.parsing.load_csv_dataframe import load_csv_dataframe, _clean_currencies  # type: ignore


def test_clean_currencies():
    assert _clean_currencies("1.234,56 €") == 1234.56
    assert _clean_currencies("  -1 234,56 ") == -1234.56
    assert _clean_currencies("1234,56 EUR") == 1234.56
    assert _clean_currencies("€1234,56") == 1234.56
    assert _clean_currencies(1234.56) == 1234.56
    assert _clean_currencies(-1234) == -1234.00


def test_clean_currencies_dataframe():
    df = pd.DataFrame(
        {
            "amount_statement": [
                "1.234,56 €",
                " -45,01 ",
                12,
            ]
        }
    )

    cleaned = df["amount_statement"].apply(_clean_currencies)

    assert isinstance(cleaned, pd.Series)
    assert cleaned.iloc[0] == 1234.56
    assert cleaned.iloc[1] == -45.01
    assert cleaned.iloc[2] == 12.0


def test_load_csv_dataframe():
    path = "src/configs/test_statement.csv"
    df = load_csv_dataframe(path)

    assert not df.empty, "DataFrame should not be empty"
    assert type(df) is pd.DataFrame, "Output should be a DataFrame"
