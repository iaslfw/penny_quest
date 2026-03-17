import numpy as np
import pandas as pd


def calculate_pocket_money(df: pd.DataFrame, key: str, multiplier: float = 2) -> float:
    """Calculates the pocket money for the month

    Args:
        df (pd.DataFrame): The data-frame of the csv-file
        key (str): Banking-key to parse csv based on template
        multiplier (float): The multiplier for the pocket money calculation

    Returns:
        float: The calculated pocket money for the month
    """
    if key not in df.columns:
        raise ValueError(f"Key '{key}' not found in DataFrame columns")

    amounts = pd.to_numeric(df[key], errors="coerce").dropna()

    # Use only expenses (negative values) for the round-up calculation.
    expenses = amounts[amounts < 0]
    expense_values = expenses.to_numpy(dtype=float)

    deltas = np.floor(expense_values) - expense_values

    pocket_money = round(float(-deltas.sum()), 2)

    return pocket_money * multiplier
