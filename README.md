# Penny Quest 🪙

Penny Quest is a Python-based CLI tool that calculates your monthly "pocket money" (or savings) by analyzing your bank statement CSVs. It automatically looks at your expenses, rounds each transaction up to the next full Euro, and sums up these difference amounts. This total is then multiplied by a custom factor (e.g., 2.0) to give you your final reward!

## Features

- Parses German-format bank CSV exports with robust encoding handling (UTF-8, Windows-1252, Latin-1).
- Vectorized, fast calculation using `pandas` and `numpy`.
- Clean CLI interface with required/optional arguments.
- Customizable multiplier to adjust your savings goal.

## Prerequisites

- [Python 3.13+](https://www.python.org/)
- [uv](https://github.com/astral-sh/uv) (for fast dependency management and execution)

## Usage

You can run the script via the command line interface using commands:

```bash
uv run main.py calculate -f <path> -k "<column_name>" [-m <factor>]
uv run main.py inspect -f <path>
```

### Commands & Arguments

**`calculate`**: Calculate your pocket money from the CSV.
- `-f`, `--file_path` (Required): Path to your bank transaction CSV file.
- `-k`, `--banking-key` (Required): The exact [banking-code](https://github.com/iaslfw/penny_quest/blob/main/src/configs/bank_list.py) of your bank.
- `-m`, `--multiplier` (Optional): A factor to multiply your saved round-ups by (Default: `2.0`).

**`inspect`**: Inspect the data in your CSV file.
- `-f`, `--file_path` (Required): Path to your bank transaction CSV file.


### Example

```bash
uv run main.py calculate -f "src/handle_csv/sheets/umsaetze_example.csv" -k "ex" -m 1.5
uv run main.py inspect -f "src/handle_csv/sheets/umsaetze_example.csv" -k "ex"
```
