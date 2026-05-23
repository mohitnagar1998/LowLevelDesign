# ATM — Low Level Design

A simulation of an ATM machine that handles card insertion, PIN authentication, balance enquiry, and cash withdrawal.

## Design Patterns Used

### State Pattern
The ATM moves through a well-defined sequence of states. Each state only allows specific operations; all others print an error. This prevents invalid transitions (e.g. withdrawing cash before authenticating).

| State | Allowed Operation |
|---|---|
| `IdleState` | `insert_card` |
| `HasCardState` | `authenticate_pin`, `exit` |
| `SelectOperationState` | `select_operation`, `exit` |
| `CashWithdrawalState` | `cash_withdrawal`, `exit` |
| `CheckBalanceState` | `display_balance`, `exit` |

### Singleton Pattern
`ATM` is a singleton — there is only one ATM machine instance. Implemented using a class-level `_atm_object` that is created once and reused on every `get_atm_object()` call.

### Chain of Responsibility Pattern
Cash dispensing delegates across a chain of denomination processors. Each processor handles as many notes of its denomination as possible, then passes the remaining amount to the next handler.

```
TwoThousandWithdrawProcessor → FiveHundredWithdrawProcessor → OneHundredWithdrawProcessor
```

## Class Structure

```
ATM.py                          # Singleton ATM machine (balance + note counts)
Card.py                         # Card with PIN validation and bank account reference
User.py                         # User who owns a Card
UserBankAccount.py              # User's bank account balance
TransactionType.py              # Enum: CASH_WITHDRAWAL, BALANCE_CHECK

ATMState.py                     # Base state (all ops default to error)
IdleState.py                    # Waiting for card
HasCardState.py                 # Card inserted, awaiting PIN
SelectOperationState.py         # PIN verified, choose transaction type
CashWithdrawalState.py          # Perform cash withdrawal
CheckBalanceState.py            # Display account balance

CashWithdrawProcessor.py        # Abstract base for chain of responsibility
TwoThousandWithdrawProcessor.py # Dispenses ₹2000 notes
FiveHundredWithdrawProcessor.py # Dispenses ₹500 notes
OneHundredWithdrawProcessor.py  # Dispenses ₹100 notes

main.py                         # Runner: sets up ATM + user and runs a withdrawal
```

## Running

```bash
python3 main.py
```

**Sample flow:** ATM loaded with ₹3500 (1×₹2000, 2×₹500, 5×₹100). User withdraws ₹2700. ATM ends with ₹800 (0×₹2000, 1×₹500, 3×₹100).
