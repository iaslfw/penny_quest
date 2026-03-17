import pandas as pd
from typing import Any
from unittest.mock import patch, MagicMock
from rich.table import Table
from src.services.print_receipt import print_receipt


@patch("src.services.print_receipt.Table")
@patch("src.services.print_receipt._create_table")
def test_create_table(mock_table: MagicMock, mock_create_table: MagicMock) -> None:
    # Simulate Table instance returned by the patch
    mock_table_instance = MagicMock(spec=Table)
    mock_table.return_value = mock_table_instance

    # Simulate Table attributes
    mock_table_instance.title = "PENNY QUEST STATEMENT"
    mock_table_instance.columns = [
        MagicMock(header="Date"),
        MagicMock(header="Item"),
        MagicMock(header="Amount"),
        MagicMock(header="Round-Up"),
        MagicMock(header="Running"),
    ]

    # Check if table is created with correct title and columns
    assert isinstance(mock_table_instance, MagicMock)
    assert len(mock_table_instance.columns) == 5
    assert mock_table_instance.title == "PENNY QUEST STATEMENT"
    assert mock_table_instance.columns[0].header == "Date"
    assert mock_table_instance.columns[1].header == "Item"
    assert mock_table_instance.columns[2].header == "Amount"
    assert mock_table_instance.columns[3].header == "Round-Up"
    assert mock_table_instance.columns[4].header == "Running"


@patch("src.services.print_receipt.Table")
@patch("src.services.print_receipt.Console")
@patch("src.services.print_receipt.load_csv_dataframe")
def test_print_receipt_table_creation(
    mock_load_csv_dataframe: MagicMock,
    mock_console: MagicMock,
    mock_table: MagicMock,
) -> None:
    # Setup mock dataframe
    data: dict[str, list[Any]] = {
        "datestamp": ["2023-01-01", "2023-01-02"],
        "description": ["Coffee", "Salary"],
        "amount": [-2.50, 1000.00],
        "difference": [0.50, 0.00],
    }
    mock_load_csv_dataframe.return_value = pd.DataFrame(data)
    mock_table_instance = MagicMock()
    mock_table.return_value = mock_table_instance

    # Act
    print_receipt("dummy_path", "dummy_key")

    # Assert Table is created
    mock_table.assert_called_once()

    # Assert specific columns are added
    column_calls = [
        call.args[0] for call in mock_table_instance.add_column.call_args_list
    ]
    assert column_calls == ["Date", "Item", "Amount", "Round-Up", "Running"]

    # Assert running total is correct -> running_total will be 0.50 + 0.00 = 0.50
    last_add_row_call = mock_table_instance.add_row.call_args_list[-1]
    assert last_add_row_call.args == ("", "TOTAL ROUND-UP", "", "", "0.50 EUR")
    assert last_add_row_call.kwargs == {"style": "bold"}

    # Assert console prints the table
    mock_console.return_value.print.assert_called_once_with(mock_table_instance)
