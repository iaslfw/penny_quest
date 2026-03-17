from src.configs.bank_list import bank_list, BankFormat

import numpy as np
import pandas as pd
import re


def _clean_currencies(num: str | int | float) -> float:
    """Cleans input and converts it to currency-number (float)

    Args:
        num (str | int | float): provided currency number as string, int or float

    Returns:
        float: cleaned currency amount
    """
    if isinstance(num, str):
        num = num.strip().replace(" ", "").replace(".", "").replace(",", ".")
        num = re.sub(r"[^\d.-]", "", num)

        return float(num.replace(",", "."))

    return float(num)


def _get_bank_data(key: str) -> BankFormat:
    """Maps key of bank to specific bank-object from list

    Args:
        key (str): abbreviation of the bank to get the specific format for parsing the csv file

    Raises:
        ValueError: In case the bank with the provided abbreviation is not found in the bank list

    Returns:
        BankFormat: The specific bank format for parsing the CSV file
    """
    for bank in bank_list:
        if bank["abb"] == key:
            selected_bank = BankFormat(
                name=bank["name"],
                abb=bank["abb"],
                drop_tables=bank["drop_tables"],
                amount_column=bank["amount_column"],
                date_column=bank["date_column"],
                description_column=bank["description_column"],
                separator=bank["separator"],
                encoding=bank["encoding"],
            )
            return selected_bank

    raise ValueError(f"Bank with abbreviation '{key}' not found in bank list")


def load_csv_dataframe(file_path: str, bank_key: str = "ex") -> pd.DataFrame:
    """Loads a CSV file into a pandas DataFrame.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        pd.DataFrame: A DataFrame containing the data from the CSV file.
    """
    try:
        bank = _get_bank_data(bank_key)  # Default to Example Bank format

        df = pd.read_csv(
            file_path,
            sep=bank["separator"],
            encoding=bank["encoding"],
            dtype=str,
            parse_dates=True,
        )

        # Strip whitespace from column names and rename them to standard names
        df = df.loc[:, df.columns != ""]
        df.columns = df.columns.str.strip().str.replace('"', "").str.replace("'", "")
        df = df.drop(columns=bank["drop_tables"])
        df = df.dropna(axis=1, how="all")
        df = df.rename(
            columns={
                bank["date_column"]: "datestamp",
                bank["description_column"]: "description",
                bank["amount_column"]: "amount",
            }
        )

        df["amount"] = df["amount"].apply(_clean_currencies).astype("float64")

        amounts = df["amount"]

        df["difference"] = np.where(amounts < 0, amounts - np.floor(amounts), 0.0)
        df["is_spending"] = pd.Series(df["amount"] < 0, index=df.index)

        return df

    except Exception as e:
        print(f"Error transforming CSV file:\n{e}")
        raise
