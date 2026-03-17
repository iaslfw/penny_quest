"""

List of Bankings with their specific formats for parsing the csv files.
If you're reading this, extend it with your bank and create a pull request.

Thanks! <3

"""

from src.configs.custom_types import BankFormat


bank_list: list[BankFormat] = [
    {
        "name": "Example Bank",
        "abb": "ex",
        "drop_tables": ["Wertstellung (Valuta)", "Vorgang"],
        "amount_column": "Umsatz in EUR",
        "date_column": "Buchungstag",
        "description_column": "Buchungstext",
        "separator": ";",
        "encoding": "latin-1",
    },
    {
        "name": "ComDirect",
        "abb": "cd",
        "drop_tables": ["Wertstellung (Valuta)", "Vorgang"],
        "amount_column": "Umsatz in EUR",
        "date_column": "Buchungstag",
        "description_column": "Buchungstext",
        "separator": ";",
        "encoding": "latin-1",
    },
    {
        "name": "VR Bank",
        "abb": "vr",
        "drop_tables": [
            "Bezeichnung Auftragskonto",
            "IBAN Auftragskonto",
            "BIC Auftragskonto",
            "Bankname Auftragskonto",
            "Valutadatum",
            "Name Zahlungsbeteiligter",
            "IBAN Zahlungsbeteiligter",
            "BIC (SWIFT-Code) Zahlungsbeteiligter",
            "Buchungstext",
            "Waehrung",
            "Saldo nach Buchung",
            "Bemerkung",
            "Gekennzeichneter Umsatz",
            "Glaeubiger ID",
            "Mandatsreferenz",
        ],
        "date_column": "Buchungstag",
        "description_column": "Verwendungszweck",
        "amount_column": "Betrag",
        "separator": ";",
        "encoding": "latin-1",
    },
]
