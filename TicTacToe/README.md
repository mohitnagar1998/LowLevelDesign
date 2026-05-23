# Tic Tac Toe — Low Level Design

An interactive two-player Tic Tac Toe game for an n×n board, with O(1) win detection per move.

## Design Patterns Used

| Pattern | Where |
|---|---|
| MVC Pattern | `Board` (model/view) + `Game` (controller) + `Player` (model) cleanly separated |
| Enum | `PieceType` (X, O) for type-safe playing pieces |

### MVC Pattern
Responsibilities are cleanly split across three classes:

| Class | Role |
|---|---|
| `Board` | **Model + View** — owns the grid, enforces placement rules, prints the board |
| `Game` | **Controller** — drives the turn loop, tracks win/draw state, rotates players |
| `Player` | **Model** — pure data object (name + playing piece) |

No class reaches into another's internals. `Game` calls `Board.add_piece` and `Board.is_full`; it never reads `board.board` directly.

### O(1) Win Detection
Instead of scanning the whole board after every move (O(n²)), `Game` maintains per-player counters for each row, column, main diagonal, and anti-diagonal. A win is detected in O(1) by checking if any counter reaches `n`:

```
rows[player][row]       — pieces placed in each row
cols[player][col]       — pieces placed in each column
diag[player]            — pieces on the main diagonal (x == y)
anti_diag[player]       — pieces on the anti-diagonal (x + y == n-1)
```

### Enum
`PieceType` (`X`, `O`) is a Python `Enum` used as the marker stored in board cells, giving a clear string representation and preventing invalid piece values.

## Class Structure

```
PlayingPiece.py   # PieceType enum: X, O
Player.py         # Player with a name and a PieceType
Board.py          # n×n grid; add_piece with bounds + occupancy checks; is_full
Game.py           # Turn loop, O(1) win detection, draw detection
main.py           # Runner: creates two players and starts the game
```

## Running

```bash
python3 main.py
```

The game is interactive — it prompts each player for a row and column on every turn, prints the board after each move, and announces the winner or a draw.
