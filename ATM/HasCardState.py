from ATMState import ATMState


class HasCardState(ATMState):

    def __init__(self):
        print("enter your card pin number")

    def authenticate_pin(self, atm, card, pin):
        is_correct = card.is_correct_pin_entered(pin)
        if is_correct:
            from SelectOperationState import SelectOperationState
            atm.set_current_atm_state(SelectOperationState())
        else:
            print("Invalid PIN Number")
            self.exit(atm)

    def exit(self, atm):
        self.return_card()
        from IdleState import IdleState
        atm.set_current_atm_state(IdleState())
        print("Exit happens")

    def return_card(self):
        print("Please collect your card")
