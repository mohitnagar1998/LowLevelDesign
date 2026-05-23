from ATMState import ATMState


class CheckBalanceState(ATMState):

    def display_balance(self, atm, card):
        print("Your Balance is:", card.get_bank_balance())
        self.exit(atm)

    def exit(self, atm):
        self.return_card()
        from IdleState import IdleState
        atm.set_current_atm_state(IdleState())
        print("Exit happens")

    def return_card(self):
        print("Please collect your card")
