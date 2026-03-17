from src.parsing.load_csv_dataframe import load_csv_dataframe
from src.services.calculate_pm import calculate_pocket_money
from src.services.print_receipt import print_receipt

from src.cli.get_cli_data import get_cli_data
from src.configs.logger import get_logger


logger = get_logger(__name__)


def main() -> None:
    command, file_path, key, multiplyer = get_cli_data()

    match command:
        case "calculate":
            # Calculate just print
            logger.info(f"Loading data from file: {file_path} with bank key: {key}")
            test_path = "src/configs/test_statement.csv"

            logger.info(
                f"Calculating pocket money from file: {file_path} with multiplier {multiplyer}"
            )

            if not key:
                raise ValueError("Banking key is required for the calculate command")

            data = load_csv_dataframe(test_path, key)

            base_pocket_money = calculate_pocket_money(data, "amount", 1.0)
            multiplied_pocket_money = round(
                base_pocket_money * (multiplyer or 2.0), 2
            )  # Using the provided multiplier

            summary_lines = [
                "\n" + "=" * 50,
                "POCKET MONEY SUMMARY",
                "=" * 50,
                f"Base amount:       {base_pocket_money:>10.2f} EUR",
                f"Multiplier:        x{multiplyer or 2.0}",
                "-" * 50,
                f"Final amount:      {multiplied_pocket_money:>10.2f} EUR",
                "=" * 50,
                "\n",
            ]
            print("\n".join(summary_lines))

        case "inspect":
            # Show overview
            if not key:
                raise ValueError("Banking key is required for the calculate command")

            logger.info(f"Showing overview for file: {file_path}")
            print_receipt(path_name=file_path, key=key)

        case _:
            logger.error(
                f"Invalid multiplier value: {multiplyer}. Expected 1.0 or 2.0."
            )
            raise ValueError(
                f"Invalid multiplier value: {multiplyer}. Expected 1.0 or 2.0."
            )


if __name__ == "__main__":
    main()
