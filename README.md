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

---

Here is a master list of ideas to level up Penny Quest, categorized from robustness to exciting new features. Since you already laid down a solid technical foundation (vectorized pandas math, CLI args, GitHub Actions), you are in a great position to build these out!

### 🛡️ Robustness & Code Quality
1. **Actually Write the Tests:** You have `pytest` installed and a pipeline ready. Add tests for:
   * Parsing weird number formats (e.g., empty strings, `0,00`, `1.000.000,50`).
   * Edge cases in `.csv` files (missing columns, completely empty files).
   * Checking that positive transactions (income) are strictly ignored in the `calculate_pocket_money` logic.
2. **Linting & Formatting in CI:** Add `ruff` (the modern, blazingly fast Python linter) and `mypy` for strict type checking. Run them in your GitHub action before `pytest`.
3. **Structured Logging:** Replace `print` statements (except your final UI output) with the `logging` module or the `rich` library. This is super helpful when reading messy CSVs without cluttering the user's screen.

### 🏦 Data Pipeline & Capabilities
4. **Auto-Detect Bank Formats (No more `-k` needed):**
   * Instead of making the user guess the column key (`"Umsatz in EUR"`), create "Bank Profiles". 
   * Auto-detect if the CSV comes from Sparkasse, Comdirect, DKB, N26, or Revolut based on the header names or let the user pass a flag like `--bank dkb`. 
   * Each profile automatically knows the delimiter (`;` vs `,`) and the correct amount/date columns.
5. **Date Ranges / Month Filtering:**
   * Usually, bank exports contain multiple months. Add `--month 02` and `--year 2026` flags.
   * *Implementation:* Parse the `Buchungstag` (Booking Date) into `datetime` objects and filter the DataFrame before doing the math.
6. **Smart Exclusions (Blocklist):**
   * You don't want to round up your rent (`Miete`) or insurance (`Versicherung`). 
   * Add a `--exclude` flag or read an `exclusions.txt` file holding keywords. Filter out rows matching those words in `Buchungstext`/`Vorgang`.

### 🚀 "Cool" Features & UX
7. **Rich Terminal UI (TUI):**
   * Use the `rich` library to make your terminal output beautiful. You can add syntax-highlighted tables showing the top 5 biggest round-up contributors, emojis, and progress bars.
8. **Persistent SQLite Storage:**
   * Instead of starting from `0` every time you run the script, save the end result in a local `sqlite3` database. 
   * You could run `penny-quest history` to see how much pocket money you saved over the entire year!
9. **Savings Goals:**
   * Add a target goal via CLI (e.g., `--goal 100`).
   * The summary then outputs a progress bar: `Savings: 45.50€ / 100.00€ [██████░░░░░] 45.5%`
10. **Detailed Breakdown Export:** 
    * Add a `--export out.json` or `--export breakdown.txt` flag that generates a receipt showing exactly which transactions contributed how much to the pocket money pool.

### Where to start?
If you want to focus on **Robustness** first: I recommend setting up **`ruff`** and writing **two basic `pytest` unit tests**.
If you want to focus on **Features** first: I highly recommend building the **Date Filtering** and **Smart Exclusions**, because they make the math much more realistic for a real-world use case.

Which direction sounds the most fun to you?