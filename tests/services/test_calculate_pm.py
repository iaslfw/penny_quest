from src.services.calculate_pm import calculate_pocket_money
from src.parsing.load_csv_dataframe import load_csv_dataframe  # type: ignore


def test_calculate_pocket_money():
    path = "src/configs/test_statement.csv"
    df = load_csv_dataframe(path, "ex")

    print(df.head())  # Debug: Print the first few rows of the DataFrame

    pocket_money = calculate_pocket_money(df, "amount")

    assert isinstance(pocket_money, float), "Pocket money should be a float"
    assert pocket_money >= 0, "Pocket money should be greater or equal to zero"
