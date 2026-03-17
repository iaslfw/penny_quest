from _pytest.monkeypatch import MonkeyPatch
from src.cli.get_cli_data import get_cli_data


def test_get_cli_calc_data(monkeypatch: MonkeyPatch):
    args = [
        "program_name",
        "calculate",
        "-f",
        "test.csv",
        "-k",
        "Amount",
        "-m",
        "2.5",
    ]

    monkeypatch.setattr("sys.argv", args)

    cmd, file_path, key, _ = get_cli_data()

    assert cmd != "", "Command should not be empty"
    assert cmd == "calculate"

    assert file_path != "", "Input file should not be empty"
    assert file_path == "test.csv"
    assert type(file_path) is str

    assert key != "", "Key should not be empty"
    assert key == "Amount"
    assert type(key) is str


def test_get_cli_inspect_data(monkeypatch: MonkeyPatch):
    args = ["program_name", "inspect", "-f", "test.csv", "-k", "ex"]

    monkeypatch.setattr("sys.argv", args)

    cmd, file_path, key, _ = get_cli_data()

    assert type(cmd) is str
    assert cmd != "", "Command should not be empty"
    assert cmd == "inspect"

    assert type(file_path) is str
    assert file_path != "", "Input file should not be empty"
    assert file_path == "test.csv"

    assert key == "ex"
