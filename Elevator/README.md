# Elevator — Low Level Design

A simulation of a multi-elevator building system. Handles external floor requests (up/down buttons on each floor) and internal cabin requests (floor buttons inside the elevator).

## Design Patterns Used

| Pattern | Where |
|---|---|
| Strategy Pattern | `ExternalDispatcher` / `InternalDispatcher` encapsulate routing logic |
| Factory Pattern | `ElevatorCreator` builds and wires all elevator cars + controllers |
| Observer / Registry Pattern | `ElevatorRegistry` decouples dispatchers from individual controllers |
| State Pattern | `ElevatorState` enum (MOVING / IDLE) drives car behaviour |

### Strategy Pattern
`ExternalDispatcher` and `InternalDispatcher` encapsulate the algorithm for deciding which elevator controller handles a given request. The routing strategy (e.g. even floor → even elevator id) is isolated in one place and can be swapped without touching any other class.

### Factory Pattern
`ElevatorCreator` is responsible for constructing `ElevatorCar` and `ElevatorController` instances and registering them in the shared registry. The rest of the system never calls constructors directly.

### Observer / Registry Pattern
`ElevatorRegistry` is a shared module-level list of all active `ElevatorController` instances. Dispatchers read from this registry rather than holding direct references to individual elevators, keeping the system loosely coupled and easy to extend with more elevators.

### State Pattern
`ElevatorState` (MOVING / IDLE) is attached to each `ElevatorCar`. The car's behaviour — whether it opens doors, accepts requests, or moves — depends on its current state.

### Priority Queue Scheduling
`ElevatorController` uses two heaps to schedule stops efficiently:
- **min-heap** for UP direction requests (serve lowest floor first)
- **max-heap** (negated values) for DOWN direction requests (serve highest floor first)

This mirrors real elevator scheduling (SCAN / elevator algorithm).

## Class Structure

```
ElevatorState.py        # Enum: MOVING, IDLE  (State Pattern)
Direction.py            # Enum: UP, DOWN
Floor.py                # Floor with external up/down buttons
ElevatorCar.py          # Physical car (id, current floor, state, door, display)
ElevatorDoor.py         # Door open/close behaviour
ElevatorDisplay.py      # Shows current floor and direction
InternalButtons.py      # Buttons inside the cabin (floor selection)
ElevatorController.py   # Scheduling logic with min/max-heap queues
ElevatorRegistry.py     # Shared list of all controllers  (Registry)
ElevatorCreator.py      # Factory: creates cars + controllers
ExternalDispatcher.py   # Strategy: routes floor-level button presses
InternalDispatcher.py   # Strategy: routes cabin button presses
Building.py             # Composes floors and wires up dispatchers
main.py                 # Runner: creates building and processes requests
```

## Running

```bash
python3 main.py
```

**Sample flow:** 5-floor building with 2 elevators. Floor 1 requests UP, floor 2 requests DOWN. Each controller processes its queue for two rounds.
