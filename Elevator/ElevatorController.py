import heapq
from Direction import Direction
from typing import List


class ElevatorController:
    def __init__(self, elevator_car):
        self.elevator_car = elevator_car
        # min-heap for up requests
        self.up_min_pq: List[int] = []
        # max-heap for down requests: store negatives to simulate max-heap
        self.down_max_pq: List[int] = []
        self.internal_requests: List[int] = []

    def submit_external_request(self, floor: int, direction: Direction):
        if direction == Direction.DOWN:
            heapq.heappush(self.down_max_pq, -floor)
            print(f"[controller {self.elevator_car.id}] external down request added: {floor}")
        else:
            heapq.heappush(self.up_min_pq, floor)
            print(f"[controller {self.elevator_car.id}] external up request added: {floor}")

    def submit_internal_request(self, floor: int):
        # internal requests append to internal queue
        self.internal_requests.append(floor)
        print(f"[controller {self.elevator_car.id}] internal request added: {floor}")

    def has_pending_request(self) -> bool:
        return bool(self.up_min_pq or self.down_max_pq or self.internal_requests)

    def process_next_request(self):
        # simple approach prefer internal reqs, then up, then down
        if self.internal_requests:
            dest = self.internal_requests.pop()
            print(f"[controller {self.elevator_car.id}] processing internal request -> {dest}")
            self.elevator_car.move_elevator(dest)
            return

        if self.elevator_car.elevator_direction.name == "UP" or self.up_min_pq:
            if self.up_min_pq:
                dest = heapq.heappop(self.up_min_pq)
                print(f"[controller {self.elevator_car.id}] processing up request -> {dest}")
                self.elevator_car.move_elevator(dest)
                return

        if self.internal_requests:
            dest = -heapq.heappop(self.down_max_pq)
            print(f"[controller {self.elevator_car.id}] processing down request -> {dest}")
            self.elevator_car.move_elevator(dest)
            return

        # nothing to do
        print(f"[controller {self.elevator_car.id}] no requests to process")