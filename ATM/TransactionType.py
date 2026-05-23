from enum import Enum


class TransactionType(Enum):
    CASH_WITHDRAWAL = "CASH_WITHDRAWAL"
    BALANCE_CHECK = "BALANCE_CHECK"

    @staticmethod
    def show_all_transaction_types():
        for t in TransactionType:
            print(t.name)
