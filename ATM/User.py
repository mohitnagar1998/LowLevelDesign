class User:
    def __init__(self):
        self.card = None
        self.bank_account = None

    def get_card(self):
        return self.card

    def set_card(self, card):
        self.card = card
