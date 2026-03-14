import numpy as np
import pandas as pd


def convert_csv(file_path: str) -> pd.DataFrame:
    """Converts csv-file into a data-frame

    Args:
        file_path (str): Path of the csv-file

    Returns:
        pd.DataFrame: the cleaned data-frame of the csv-file
    """

    df: pd.DataFrame = pd.read_csv(
        file_path,
        sep=";",
        encoding="latin-1",
        dtype=str,
    )

    # Keep df as a DataFrame and only normalize its column labels.
    df.columns = df.columns.str.strip()

    df = df.loc[:, df.columns != ""]
    df = df.dropna(axis=1, how="all")

    return df


def calculate_pocket_money(df: pd.DataFrame, key: str, multiplier: float = 2) -> float:
    """Calculates the pocket money for the month

    Args:
        df (pd.DataFrame): The data-frame of the csv-file
        key (str): The column name containing the transaction amounts
        multiplier (float): The multiplier for the pocket money calculation

    Returns:
        float: The calculated pocket money for the month
    """
    if key not in df.columns:
        raise KeyError(f"Column '{key}' not found in DataFrame")

    amounts = pd.to_numeric(
        df[key]
        .astype("string")
        .str.replace(".", "", regex=False)
        .str.replace(",", ".", regex=False),
        errors="coerce",
    ).dropna()

    # Use only expenses (negative values) for the round-up calculation.
    expenses = amounts[amounts < 0]
    expense_values = expenses.to_numpy(dtype=float)
    deltas = np.floor(expense_values) - expense_values
    pocket_money = round(float(-deltas.sum()), 2)

    return pocket_money * multiplier
