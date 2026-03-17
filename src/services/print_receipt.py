from src.configs.logger import get_logger
from src.parsing.load_csv_dataframe import load_csv_dataframe
from rich import box
from rich.console import Console
from rich.table import Table

logger = get_logger(__name__)


def _create_table() -> Table:
    table = Table(
        title="PENNY QUEST STATEMENT",
        caption="Thank you for using Penny Quest",
        box=box.SIMPLE,
        safe_box=True,
        show_lines=True,
        header_style="bold",
        title_style="bold",
        caption_style="dim",
        pad_edge=True,
        border_style="dim",
    )
    table.add_column("Date", no_wrap=True)
    table.add_column("Item", overflow="fold")
    table.add_column("Amount", justify="right", no_wrap=True)
    table.add_column("Round-Up", justify="right", style="green", no_wrap=True)
    table.add_column("Running", justify="right", style="green", no_wrap=True)

    return table


def print_receipt(path_name: str, key: str = "ex") -> None:
    df = load_csv_dataframe(path_name, key)
    df = df[["datestamp", "description", "amount", "difference"]]

    console = Console()

    table = _create_table()

    running_total = 0.0
    records = df.astype({"amount": "float64", "difference": "float64"}).itertuples(
        index=False
    )

    for row in records:
        date = str(row.datestamp).strip()
        description = str(row.description).strip().replace('"', "")
        amount = float(row.amount)  # type: ignore
        diff = float(row.difference)  # type: ignore

        running_total += diff

        table.add_row(
            date,
            description,
            f"{amount:,.2f} EUR",
            f"{diff:.2f} EUR",
            f"{running_total:.2f} EUR",
            style="dim" if amount > 0 else "",
        )

    table.add_section()
    table.add_row(
        "",
        "TOTAL ROUND-UP",
        "",
        "",
        f"{running_total:.2f} EUR",
        style="bold",
    )

    console.print(table)
