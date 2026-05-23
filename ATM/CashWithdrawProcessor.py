class CashWithdrawProcessor:

    def __init__(self, next_cash_withdrawal_processor):
        self.next_cash_withdrawal_processor = next_cash_withdrawal_processor

    def withdraw(self, atm, remaining_amount):
        if self.next_cash_withdrawal_processor is not None:
            self.next_cash_withdrawal_processor.withdraw(atm, remaining_amount)
