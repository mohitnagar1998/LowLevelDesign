from Floor import Floor
from Direction import Direction
from Building import Building
from ElevatorRegistry import elevator_controller_list


def main():
    floor_list = [Floor(i) for i in range(1, 6)]
    buiding = Building(floor_list)
    print(f"building created with floors:", [f.floor_number for f in floor_list])

    floor_list[0].press_button(Direction.UP)
    floor_list[1].press_button(Direction.DOWN)
    # floor_list[7].press_button(Direction.UP)

    print("processing controller queues (one pass each)")
    for controller in elevator_controller_list:
        controller.process_next_request()

    for controller in elevator_controller_list:
        controller.process_next_request()

if __name__ == "__main__":
    main()

