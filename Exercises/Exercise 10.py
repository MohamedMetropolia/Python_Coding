# Assignment 10.1
class Elevator:
    def __init__(self, top, bottom, current):
        self.top = top
        self.bottom = bottom
        self.current = current

    # Function that prevents the elevator from going over the max and allows it to go up
    def floor_up(self):
        self.current += 1

    # Function that prevents the elevator from going below the min and allows it to go down
    def floor_down(self):
        self.current -= 1

    # Function that moves through the floors while giving output.
    def go_to_floor(self, floor):
        while floor > self.current:  # if the input floor is higher than the current floor, moves the elevator up
            print(f"current floor: {self.current}")
            self.floor_up()
        if floor == self.current:  # stops the elevator at the right floor
            print(f"current floor: {self.current}")
        else:
            while floor < self.current:  # if the input floor is lower than the current floor, moves the elevator down
                self.floor_down()
                print(f"current floor: {self.current}")

# Assignment 10.2
class Building:
    def __init__(self, bottom, top, num_elevators):
        self.bottom = bottom
        self.top = top
        self.current = bottom
        self.num_elevators = num_elevators
        self.elevator_list = []

    def run_elevator(self, num_ele, tar_flr):
        for i in range(self.num_elevators):
            self.elevator_list.append(Elevator(self.top, self.bottom, self.current))
        self.elevator_list[num_ele].go_to_floor(tar_flr)

# Assignment 10.3
    def fire_alarm(self):
        for elevator in self.elevator_list:
            if elevator.current == self.bottom:
                continue
            elevator.go_to_floor(self.bottom)
            print(f"current floor: {self.current}")

h = Elevator(1, 10, 1)
h.go_to_floor(9)

b = Building(1, 10, 3)
b.run_elevator(2, 4)
b.fire_alarm()

# Assignment 10.4 is in Exercise 9
