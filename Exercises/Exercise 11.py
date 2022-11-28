from abc import ABC, abstractmethod


# Assignment 11.1
class Publication(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def print_information(self):
        pass


class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        print(f"{self.name} ({self.author}, {self.page_count} pages) ")


class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_ed = chief_editor

    def print_information(self):
        print(f"{self.name} (chief editor {self.chief_ed})")


if __name__ == '__main__':
    mag = Magazine("life of me", "jäätelö")
    book = Book("Compartment No. 6", "author me", 192)
    mag.print_information()
    book.print_information()


# Assignment 11.2
class Car:
    def __init__(self, reg_num: str, max_spd: int, current_spd=0, dist=0):
        self.name = reg_num
        self.max_spd = max_spd
        self.current_spd = current_spd
        self.dist = dist

    def accelerate(self, acceleration):
        self.change = acceleration
        self.current_spd += self.change
        if self.current_spd < 0:
            self.current_spd = 0
        elif self.current_spd > self.max_spd:
            self.current_spd = self.max_spd

    def drive(self, time):
        self.dist += self.current_spd * time


class ElectricCar(Car):
    def __init__(self, reg_num, max_spd, bat_cap):
        super().__init__(reg_num, max_spd)
        self.battery = bat_cap


class GasolineCar(Car):
    def __init__(self, reg_num, max_spd, tank_cap):
        super().__init__(reg_num, max_spd)
        self.tank = tank_cap


car1 = ElectricCar('ABC-15', 180, 52.5)
car2 = GasolineCar('ACD-123', 165, 32.3)

Speed = int(input("Enter the speed of the cars: "))
Time = int(input("Enter the amount of hours: "))
print("")

car1.accelerate(Speed)
car2.accelerate(Speed)
car1.drive(Time)
car2.drive(Time)

print(f'For car {car1.name}\n'
      f'Max speed={car1.max_spd}\n'
      f'Current speed:{car1.current_spd}\n'
      f'Distance:{car1.dist}\n'
      f'Kw/h usage: {car1.battery * Time}\n')

print(f'For car {car2.name}\n'
      f'Max speed={car2.max_spd}\n'
      f'Current speed:{car2.current_spd}\n'
      f'Distance:{car2.dist}\n'
      f'Fuel usage: {(car2.tank * Time):.2f}')
