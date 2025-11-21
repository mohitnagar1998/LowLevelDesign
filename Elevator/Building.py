from typing import List
from Floor import Floor


class Building:
    def __init__(self, floors: List[Floor]):
        self.floor_list = floors

    def addFloor(self, new_floor: Floor):
        self.floor_list.append(new_floor)

    def remove_floor(self, remove_floor: Floor):
        self.floor_list.remove(remove_floor)

    def get_all_floor_list(self):
        return self.floor_list
