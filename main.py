from src.handle_data.csv_reader import convert_csv, calculate_pocket_money
from src.cli.get_cli_data import get_cli_data


def main():
    file_path, key, multiplier = get_cli_data()

    data = convert_csv(str(file_path))

    base_pocket_money = calculate_pocket_money(data, key, 1.0)
    multiplied_pocket_money = round(base_pocket_money * multiplier, 2)

    summary_lines = [
        "\n" + "=" * 50,
        "POCKET MONEY SUMMARY",
        "=" * 50,
        f"Base amount:       {base_pocket_money:>10.2f} EUR",
        f"Multiplier:        x{multiplier:g}",
        "-" * 50,
        f"Final amount:      {multiplied_pocket_money:>10.2f} EUR",
        "=" * 50,
    ]
    print("\n".join(summary_lines))


if __name__ == "__main__":
    main()
