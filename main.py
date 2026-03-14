from src.handle_csv.csv_reader import convert_csv, calculate_pocket_money


def main():
    key = str(input("Enter the column name containing the transaction amounts: "))
    multiplier_input = float(
        input("Enter the multiplier for the pocket money calculation (default is 2): ")
    )
    multiplier = multiplier_input if multiplier_input else 2

    data = convert_csv("src/handle_csv/sheets/umsaetze_example.csv")

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
