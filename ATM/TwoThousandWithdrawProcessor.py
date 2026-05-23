from CashWithdrawProcessor import CashWithdrawProcessor


class TwoThousandWithdrawProcessor(CashWithdrawProcessor):

    def __init__(self, next_cash_withdraw_processor):
        super().__init__(next_cash_withdraw_processor)

    def withdraw(self, atm, remaining_amount):
        required = remaining_amount // 2000
        balance = remaining_amount % 2000

        if required <= atm.get_no_of_two_thousand_notes():
            atm.deduct_two_thousand_notes(required)
        else:
            balance = balance + (required - atm.get_no_of_two_thousand_notes()) * 2000
            atm.deduct_two_thousand_notes(atm.get_no_of_two_thousand_notes())

        if balance != 0:
            super().withdraw(atm, balance)
