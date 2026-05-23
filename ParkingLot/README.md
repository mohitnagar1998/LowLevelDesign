# Parking Lot — Low Level Design

A simulation of a parking lot management system. Handles parking and unparking vehicles across different spot types.

## Design Patterns Used

| Pattern | Where |
|---|---|
| Abstract Class / Template Method Pattern | `ParkingSpot` and `ParkingSpotManager` define shared behaviour; subclasses specialise |
| Factory Pattern | `ParkingSpotManagerFactory` creates the right manager for a vehicle type |
| Enum | `VehicleType` for type-safe vehicle categories |

### Abstract Class / Template Method Pattern
`ParkingSpot` is an abstract base class (Python `ABC`) that implements the common `park_vehicle` / `unpark_vehicle` logic once. Subclasses (`TwoWheelerParkingSpot`, `ThreeWheelerParkingSpot`) only override the abstract `price()` method — the template — without duplicating any parking logic.

The same pattern applies to `ParkingSpotManager`: shared `find_parking_space` logic lives in the abstract base; `TwoWheelerParkingSpotManager` and `FourWheelerParkingSpotManager` are concrete specialisations for each vehicle category.

### Factory Pattern
`ParkingSpotManagerFactory.getParkingManager(parkingType)` creates and returns the correct `ParkingSpotManager` subclass based on a string input (`"twowheeler"` / `"fourwheeler"`). The caller never instantiates managers directly, keeping creation logic in one place.

### Enum
`VehicleType` (`CAR`, `BIKE`) is a Python `Enum` used when constructing `Vehicle` instances, preventing invalid type strings.

## Class Structure

```
Vehicle.py              # Vehicle with number and VehicleType enum
ParkingSpot.py          # Abstract base (park/unpark); TwoWheeler + ThreeWheeler subclasses
ParkingSpotManager.py   # Abstract manager (find_parking_space); TwoWheeler + FourWheeler
                        # subclasses; ParkingSpotManagerFactory
Ticket.py               # Parking ticket (vehicle, spot, entry/exit timestamps)
```

## Key Relationships

```
ParkingSpotManagerFactory
    └── creates → TwoWheelerParkingSpotManager | FourWheelerParkingSpotManager
                        └── manages → ParkingSpot(s)
                                          └── parks → Vehicle
                                          └── issues → Ticket
```
