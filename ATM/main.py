from ATM import ATM
from User import User
from Card import Card
from UserBankAccount import UserBankAccount
from TransactionType import TransactionType


def create_bank_account():
    bank_account = UserBankAccount()
    bank_account.balance = 3000
    return bank_account


def create_card():
    card = Card()
    card.set_bank_account(create_bank_account())
    return card


def create_user():
    user = User()
    user.set_card(create_card())
    return user


def initialize():
    atm = ATM.get_atm_object()
    atm.set_atm_balance(3500, 1, 2, 5)

    user = create_user()
    return atm, user


if __name__ == "__main__":
    atm, user = initialize()

    atm.print_current_atm_status()
    atm.get_current_atm_state().insert_card(atm, user.card)
    atm.get_current_atm_state().authenticate_pin(atm, user.card, 112211)
    atm.get_current_atm_state().select_operation(atm, user.card, TransactionType.CASH_WITHDRAWAL)
    atm.get_current_atm_state().cash_withdrawal(atm, user.card, 2700)
    atm.print_current_atm_status()
