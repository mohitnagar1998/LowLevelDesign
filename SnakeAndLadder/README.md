# Snake and Ladder — Low Level Design

A simulation of the classic Snake and Ladder board game for two players on a 10×10 grid with randomly placed snakes and ladders.

## Design Patterns Used

| Pattern | Where |
|---|---|
| Composite Pattern | `Board` → `Cell` → `Jump` hierarchy; snakes and ladders unified as a single `Jump` type |
| Iterator Pattern | `collections.deque` used for O(1) round-robin player turn management |

### Composite Pattern
The board is modelled as a hierarchy of composable objects:
- `Board` contains a 2D grid of `Cell` objects
- Each `Cell` optionally holds one `Jump` object
- A `Jump` with `end > start` is a **ladder**; `end < start` is a **snake**

This unifies snakes and ladders into a single type (`Jump`) instead of maintaining two separate lists. `Game` just checks `cell.jump` — it does not need to know whether the jump is a snake or a ladder until it prints the message.

### Iterator Pattern (Round-Robin via Deque)
Player turns are managed with a `collections.deque`. On each turn, the current player is popped from the front and appended to the back after their move — a clean O(1) round-robin without index arithmetic.

## Class Structure

```
Jump.py      # Snake or ladder: start → end  (end < start = snake, end > start = ladder)
Cell.py      # Single board cell; optionally holds one Jump
Board.py     # 10×10 grid of Cells; randomly places snakes and ladders on init
Dice.py      # Rolls n dice with configurable min/max face values
Player.py    # Player with an id and current board position
Game.py      # Turn loop, dice roll, jump resolution, win detection
main.py      # Runner: creates and starts the game
```

## Running

```bash
python3 main.py
```

**Sample flow:** 10×10 board with 5 snakes and 4 ladders placed randomly. Two players (p1, p2) alternate turns until one reaches or passes cell 99.
