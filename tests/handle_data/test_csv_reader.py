import pandas as pd
from src.handle_data.csv_reader import convert_csv, calculate_pocket_money


def test_convert_csv():
    path = "tests/mocks/test.csv"
    df = convert_csv(path)

    assert not df.empty, "DataFrame should not be empty"
    assert type(df) is pd.DataFrame, "Output should be a DataFrame"


def test_calculate_pocket_money():
    path = "tests/mocks/test.csv"
    df = convert_csv(path)

    pocket_money = calculate_pocket_money(df, "Umsatz", 2)

    assert isinstance(pocket_money, float), "Pocket money should be a float"
    assert pocket_money >= 0, "Pocket money should be greater or equal to zero"
