from typing import TypedDict


class BankFormat(TypedDict):
    name: str
    abb: str
    drop_tables: list[str]
    amount_column: str
    date_column: str
    description_column: str
    separator: str
    encoding: str
