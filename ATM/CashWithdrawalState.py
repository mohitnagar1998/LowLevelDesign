from ATMState import ATMState
from TwoThousandWithdrawProcessor import TwoThousandWithdrawProcessor
from FiveHundredWithdrawProcessor import FiveHundredWithdrawProcessor
from OneHundredWithdrawProcessor import OneHundredWithdrawProcessor


class CashWithdrawalState(ATMState):

    def __init__(self):
        print("Please enter the Withdrawal Amount")

    def cash_withdrawal(self, atm, card, withdrawal_amount_request):
        if atm.get_atm_balance() < withdrawal_amount_request:
            print("Insufficient fund in the ATM Machine")
            self.exit(atm)
        elif card.get_bank_balance() < withdrawal_amount_request:
            print("Insufficient fund in the your Bank Account")
            self.exit(atm)
        else:
            card.deduct_bank_balance(withdrawal_amount_request)
            atm.deduct_atm_balance(withdrawal_amount_request)

            withdraw_processor = TwoThousandWithdrawProcessor(
                FiveHundredWithdrawProcessor(
                    OneHundredWithdrawProcessor(None)
                )
            )
            withdraw_processor.withdraw(atm, withdrawal_amount_request)
            self.exit(atm)

    def exit(self, atm):
        self.return_card()
        from IdleState import IdleState
        atm.set_current_atm_state(IdleState())
        print("Exit happens")

    def return_card(self):
        print("Please collect your card")
