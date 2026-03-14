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

You can run the script via the command line interface:

```bash
uv run main.py -f <file_path> -k "<column_name>" [-m <factor>]
```

### Arguments

**Required:**
- `-f`, `--file`: Path to your bank transaction CSV file.
- `-k`, `--key`: The exact column name containing the monetary transaction amounts (e.g., `"Umsatz in EUR"`).

**Optional:**
- `-m`, `--multiplier`: A factor to multiply your saved round-ups by (Default: `2.0`).

### Example

```bash
uv run main.py -f "src/handle_csv/sheets/umsaetze_example.csv" -k "Umsatz in EUR" -m 1.5
```