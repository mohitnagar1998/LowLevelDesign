class ATM:
    _atm_object = None

    def __init__(self):
        self.current_atm_state = None
        self._atm_balance = 0
        self.no_of_two_thousand_notes = 0
        self.no_of_five_hundred_notes = 0
        self.no_of_one_hundred_notes = 0

    @classmethod
    def get_atm_object(cls):
        if cls._atm_object is None:
            cls._atm_object = ATM()
        from IdleState import IdleState
        cls._atm_object.set_current_atm_state(IdleState())
        return cls._atm_object

    def set_current_atm_state(self, state):
        self.current_atm_state = state

    def get_current_atm_state(self):
        return self.current_atm_state

    def get_atm_balance(self):
        return self._atm_balance

    def set_atm_balance(self, balance, no_of_two_thousand_notes, no_of_five_hundred_notes, no_of_one_hundred_notes):
        self._atm_balance = balance
        self.no_of_two_thousand_notes = no_of_two_thousand_notes
        self.no_of_five_hundred_notes = no_of_five_hundred_notes
        self.no_of_one_hundred_notes = no_of_one_hundred_notes

    def get_no_of_two_thousand_notes(self):
        return self.no_of_two_thousand_notes

    def get_no_of_five_hundred_notes(self):
        return self.no_of_five_hundred_notes

    def get_no_of_one_hundred_notes(self):
        return self.no_of_one_hundred_notes

    def deduct_atm_balance(self, amount):
        self._atm_balance = self._atm_balance - amount

    def deduct_two_thousand_notes(self, number):
        self.no_of_two_thousand_notes = self.no_of_two_thousand_notes - number

    def deduct_five_hundred_notes(self, number):
        self.no_of_five_hundred_notes = self.no_of_five_hundred_notes - number

    def deduct_one_hundred_notes(self, number):
        self.no_of_one_hundred_notes = self.no_of_one_hundred_notes - number

    def print_current_atm_status(self):
        print("Balance:", self._atm_balance)
        print("2kNotes:", self.no_of_two_thousand_notes)
        print("500Notes:", self.no_of_five_hundred_notes)
        print("100Notes:", self.no_of_one_hundred_notes)
