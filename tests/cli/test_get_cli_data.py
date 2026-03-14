from _pytest.monkeypatch import MonkeyPatch
from src.cli.get_cli_data import get_cli_data


def test_get_cli_data(monkeypatch: MonkeyPatch):
    test_args = ["program_name", "-f", "test.csv", "-k", "Amount", "-m", "2.5"]
    monkeypatch.setattr("sys.argv", test_args)

    inFile, key, multiplier = get_cli_data()

    assert inFile != "", "Input file should not be empty"
    assert inFile == "test.csv"
    assert type(inFile) is str

    assert key != "", "Key should not be empty"
    assert key == "Amount"
    assert type(key) is str

    assert multiplier == 2.5
    assert type(multiplier) is float
