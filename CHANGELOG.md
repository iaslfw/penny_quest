# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Introduced explicit CLI subcommands (`calculate` and `inspect`) instead of implicit behavior based on the `multiplier` flag.
- Added `calculate` subcommand specifically for calculating pocket money.
- Added `inspect` subcommand for showing an overview of a given CSV file data.

### Changed
- Refactored `get_cli_data.py` to use `argparse` subparsers.
- Renamed CLI argument `--file` to `--file_path`.
- Renamed CLI argument `--key` to `--banking-key`.
- Updated `main.py` entrypoint to match on the parsed subcommands to drive internal application logic.
