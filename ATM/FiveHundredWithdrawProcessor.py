from CashWithdrawProcessor import CashWithdrawProcessor


class FiveHundredWithdrawProcessor(CashWithdrawProcessor):

    def __init__(self, next_cash_withdraw_processor):
        super().__init__(next_cash_withdraw_processor)

    def withdraw(self, atm, remaining_amount):
        required = remaining_amount // 500
        balance = remaining_amount % 500

        if required <= atm.get_no_of_five_hundred_notes():
            atm.deduct_five_hundred_notes(required)
        else:
            balance = balance + (required - atm.get_no_of_five_hundred_notes()) * 500
            atm.deduct_five_hundred_notes(atm.get_no_of_five_hundred_notes())

        if balance != 0:
            super().withdraw(atm, balance)
