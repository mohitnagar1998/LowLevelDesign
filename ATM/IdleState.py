from ATMState import ATMState


class IdleState(ATMState):

    def insert_card(self, atm, card):
        print("Card is inserted")
        from HasCardState import HasCardState
        atm.set_current_atm_state(HasCardState())
