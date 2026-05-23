from ATMState import ATMState
from TransactionType import TransactionType


class SelectOperationState(ATMState):

    def __init__(self):
        self._show_operations()

    def select_operation(self, atm, card, txn_type):
        if txn_type == TransactionType.CASH_WITHDRAWAL:
            from CashWithdrawalState import CashWithdrawalState
            atm.set_current_atm_state(CashWithdrawalState())
        elif txn_type == TransactionType.BALANCE_CHECK:
            from CheckBalanceState import CheckBalanceState
            atm.set_current_atm_state(CheckBalanceState())
        else:
            print("Invalid Option")
            self.exit(atm)

    def exit(self, atm):
        self.return_card()
        from IdleState import IdleState
        atm.set_current_atm_state(IdleState())
        print("Exit happens")

    def return_card(self):
        print("Please collect your card")

    def _show_operations(self):
        print("Please select the Operation")
        TransactionType.show_all_transaction_types()
