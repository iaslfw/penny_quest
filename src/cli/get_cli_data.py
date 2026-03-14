import argparse


def get_cli_data():
    parser = argparse.ArgumentParser(
        prog="Penny Quest",
        description="Calculate pocket money based on CSV data",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        add_help=False,
    )

    required = parser.add_argument_group("required arguments")
    optional = parser.add_argument_group("optional arguments")

    optional.add_argument(
        "-h",
        "--help",
        action="help",
        default=argparse.SUPPRESS,
        help="show this help message and exit",
    )

    required.add_argument(
        "-f",
        "--file",
        type=str,
        metavar="",
        required=True,
        help="Input CSV file",
    )
    required.add_argument(
        "-k",
        "--key",
        type=str,
        metavar="",
        required=True,
        help="Column name containing transaction amounts",
    )
    optional.add_argument(
        "-m",
        "--multiplier",
        type=float,
        metavar="",
        default=2.0,
        help="Multiplier for pocket money calculation",
    )

    args = parser.parse_args()

    inFile = args.file
    key = args.key
    multiplier = args.multiplier

    return inFile, key, multiplier
