# BookMyShow — Low Level Design

A simulation of a movie ticket booking platform. Supports adding movies and theatres across cities, browsing shows, and booking seats.

## Design Patterns Used

| Pattern | Where |
|---|---|
| MVC / Controller Pattern | `MovieController`, `TheatreController` separate business logic from models |
| Repository Pattern | Controllers act as in-memory repositories keyed by city |
| Enum | `City`, `SeatCategory` for type-safe constants |

### MVC / Controller Pattern
Business logic is separated from data models using dedicated controller classes. The runner (`BookMyShow.py`) acts as the view/entry-point, talking only to controllers. Controllers manage all access to the underlying model collections.

- `MovieController` — city → movies mapping; lookup by city or name
- `TheatreController` — city → theatres mapping; finds shows for a given movie in a city

### Repository Pattern
Each controller is effectively an in-memory repository. Data is added via `add_movie` / `add_theatre` and retrieved via query methods — the runner never holds or searches raw collections directly.

### Model-driven Design
Each real-world entity is its own class with a single responsibility:

| Entity | Responsibility |
|---|---|
| `Movie` | Movie metadata (id, name, duration) |
| `Theatre` | Owns screens and shows; belongs to a city |
| `Screen` | Owns a list of seats |
| `Show` | Links a screen + movie + start time; tracks booked seat IDs |
| `Seat` | Has an ID and a seat category (Silver/Gold/Platinum) |
| `Booking` | Records which show and which seats were booked |

### Enum
`City` and `SeatCategory` are Python `Enum` subclasses to avoid raw string comparisons across the codebase.

## Class Structure

```
enums.py              # City, SeatCategory enums
Movie.py              # Movie entity
Seat.py               # Seat entity with category
Screen.py             # Screen with a list of seats
Show.py               # Show linking screen + movie + time
Theatre.py            # Theatre with screens and shows
Booking.py            # Booking record (show + seats)
MovieController.py    # Repository + lookup for movies
TheatreController.py  # Repository + lookup for theatres/shows
BookMyShow.py         # Runner: initializes data and creates a booking
```

## Running

```bash
python3 BookMyShow.py
```

**Sample flow:** Two movies (AVENGERS, BAAHUBALI) added in Bangalore. A booking is made for BAAHUBALI seat 30 — succeeds on first attempt, rejected on second (already booked).
