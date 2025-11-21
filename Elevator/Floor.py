from Direction import Direction
from ExternalDispatcher import ExternalDispatcher

class Floor:
    def __init__(self, floor_number):
        self.floor_number = floor_number
        self.external_dispatcher = ExternalDispatcher()

    def press_button(self, direction: Direction):
        print(f"[floor] floor {self.floor_number} pressed {direction}")
        self.external_dispatcher.submit_external_request(self.floor_number, direction)