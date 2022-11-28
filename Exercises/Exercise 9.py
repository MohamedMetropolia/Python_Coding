import random

# Assignment 9.1 - 9.3
"""
class Car:
    # Function that houses the variables which we'll need later.
    def __init__(self, reg_num, max_spd):
        self.reg_num = reg_num
        self.max_spd = max_spd
        self.curr_spd = 0
        self.t_dis = 0

    # Function that allows us to change the current speed and restrict it to be below the maximum
    def accelerate(self, change_speed):
        self.curr_spd = self.curr_spd + change_speed
        if self.curr_spd > self.max_spd:
            self.curr_spd = self.max_spd
        elif self.curr_spd < 0:
            self.curr_spd = 0
    # Function that multiplies the total distance by time
    def drive(self, time):
        self.t_dis = self.t_dis + self.curr_spd * time

    # Function to print out all the variables.
    def show(self):
        print(f"Registration number: {self.reg_num}\n"
              f"Maximum speed: {self.max_spd} km/h \n"
              f"Current speed: {self.curr_spd} km/h \n"
              f"Travelled distance: {self.t_dis} km\n")

# Variable that calls the Class car and inserts parameters to be printed
newCar = Car("ABC-123", 142)
newCar.show()

# Variable that calls the accelerate function that adds current speed parameter +30, +50, -200, etc.
newCar.accelerate(30)
newCar.show()
newCar.accelerate(70)
newCar.show()
newCar.accelerate(50)
newCar.show()
newCar.accelerate(-200)
newCar.show()
newCar.accelerate(60)
newCar.show()

# Variable that calls the drive function that multiplies the total distance by time.
newCar.drive(1.5)
newCar.show()


# Assignment 9.4
car_List = []
race_cars = 0
while race_cars < 10:
    race_cars += 1
    car_List.append(Car(f"ABC-{race_cars}", random.randint(100, 200)))

max_dist = 0
while max_dist < 10000:
    for car in car_List:
        car.accelerate(random.randint(-10, 15))
        car.drive(1)
        max_dist = max(car.t_dis, max_dist)

for car in car_List:
    print(f"{car.reg_num} : {car.max_spd} km/h, {car.t_dis} km")
print(f"The winner travelled a total distance of: {max_dist} km")
"""
# Assignment 10.4
class Car:
    def __init__(self, reg_num, max_spd, cur_spd=0, trav_dst=0):
        self.reg_num = reg_num
        self.max_spd = max_spd
        self.cur_spd = cur_spd
        self.trav_dst = trav_dst

    def __str__(self):
        print(self.reg_num, self.max_spd, self.cur_spd, self.trav_dst)

    def accelerate(self, change_spd):
        self.cur_spd += change_spd
        if self.cur_spd > self.max_spd:
            self.cur_spd = self.max_spd
        elif self.cur_spd < 0:
            self.cur_spd = 0
        return self.cur_spd

    def drive(self, time):
        drive_time = self.cur_spd * time
        self.trav_dst += drive_time
        return self.trav_dst

class Race:
    def __init__(self, name, dist_km, car_list: ()):
        self.name = name
        self.car_list = car_list
        self.dist_km = dist_km
        self.winner = ''
        self.hrs_race = 0

    def hour_passes(self):
        for cars in car_list:
            cars.accelerate(random.randint(-10, 15))
            cars.drive(1)
            self.race_finished()

    def print_status(self):
        for each_car in self.car_list:
            each_car.__str__()

    def race_finished(self):
        for cars in self.car_list:
            if cars.trav_dst >= self.dist_km:
                self.winner = cars.reg_num
                return True

car_list = []
for i in range(10):
    car_list.append(Car(f"ABC-{i + 1}", random.randint(100, 200)))
    race = Race("Grand Demolition Derby", 8000, car_list)
while not race.race_finished():
    race.hrs_race += 1
    if race.hrs_race % 10 == 0:
        race.print_status()
        print(f"\n{race.hrs_race} Hours have passed!")
        print()
    else:
        race.hour_passes()
print(f"The {race.name} lasted for {race.hrs_race} hours. The winner is {race.winner}!")
race.print_status()
