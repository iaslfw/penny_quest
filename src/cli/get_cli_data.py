import argparse
from typing import Optional, Tuple


def get_cli_data() -> Tuple[str, str, Optional[str], Optional[float]]:
    parser = argparse.ArgumentParser(
        prog="Penny Quest",
        description="Calculate pocket money based on CSV data",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    subparsers = parser.add_subparsers(
        dest="command", required=True, help="Sub-commands"
    )

    # Command: calculate
    calculate_parser = subparsers.add_parser("calculate", help="Calculate pocket money")
    calculate_parser.add_argument(
        "--file_path", "-f", type=str, required=True, help="Input CSV file path"
    )
    calculate_parser.add_argument(
        "--banking-key",
        "-k",
        type=str,
        required=True,
        help="Banking key to identify CSV-template",
    )
    calculate_parser.add_argument(
        "--multiplier",
        "-m",
        type=float,
        default=2.0,
        help="Multiplier for pocket money calculation",
    )

    # Command: inspect
    inspect_parser = subparsers.add_parser("inspect", help="Inspect file data")
    inspect_parser.add_argument(
        "--file_path", "-f", type=str, required=True, help="Input CSV file path"
    )
    inspect_parser.add_argument(
        "--banking-key",
        "-k",
        type=str,
        required=True,
        help="Banking key to identify CSV-template",
    )

    args = parser.parse_args()

    return (
        args.command,
        args.file_path,
        getattr(args, "banking_key", None),
        getattr(args, "multiplier", None),
    )
