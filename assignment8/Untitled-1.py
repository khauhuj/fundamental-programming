print("---TASK 1---")
class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current_floor = bottom

    def floor_up(self):
        self.current_floor = self.current_floor + 1
        print(f"your current floor is {self.current_floor}")

    def floor_down(self):
        self.current_floor = self.current_floor - 1
        print(f"your current floor is {self.current_floor}")

    def go_to_floor(self, target):
        while self.current_floor != target:
            if self.current_floor < target:
                self.floor_up()
            else:
                self.floor_down()

skibidi = Elevator(0,10)
skibidi.go_to_floor(5)


print("---TASK 2---")
class Building:
    def __init__(self, bottom, top, number_of_elevators):
        self.bottom = bottom
        self.top = top
        self.number_of_elevators = number_of_elevators
        self.elevators = []

        for i in range(number_of_elevators):
            e = Elevator(bottom, top)
            self.elevators.append(e)

    def run_elevator(self, elevator_number, target_floor):
        print(f"Running elevator {elevator_number} to floor {target_floor}")
        self.elevators[elevator_number].go_to_floor(target_floor)


building = Building(0, 10, 3)
building.run_elevator(0, 6)
building.run_elevator(1, 3)


print("--TASK 3---")

class BuildingWithFire(Building):
    def fire_alarm(self):
        print("FIRE ALARM!!!")
        for i in range(len(self.elevators)):
            print(f"Elevator {i} going to bottom floor")
            self.elevators[i].go_to_floor(self.bottom)


building2 = BuildingWithFire(0, 10, 3)

building2.run_elevator(0, 7)
building2.run_elevator(1, 5)

building2.fire_alarm()

print("---TASK 4---")
import random

class Car:
    def __init__(self, reg_number, max_speed):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.distance = 0

    def accelerate(self, change):
        self.current_speed += change

        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.distance += self.current_speed * hours


class Race:
    def __init__(self, name, km, car_list):
        self.name = name
        self.km = km
        self.cars = car_list

    def hour_passes(self):
        for car in self.cars:
            change = random.randint(-10, 15)
            car.accelerate(change)
            car.drive(1)

    def print_status(self):
        print("\nCurrent race status:")
        print("Reg\tSpeed\tDistance")
        for car in self.cars:
            print(f"{car.reg_number}\t{car.current_speed}\t{car.distance}")

    def race_finished(self):
        for car in self.cars:
            if car.distance >= self.km:
                return True
        return False


cars = []
for i in range(10):
    car = Car(f"ABC-{i+1}", random.randint(100, 200))
    cars.append(car)

race = Race("Grand Demolition Derby", 8000, cars)

hours = 0

while not race.race_finished():
    hours += 1
    race.hour_passes()

    if hours % 10 == 0:
        print(f"\n--- Hour {hours} ---")
        race.print_status()


print(f"\n--- Race finished in {hours} hours ---")
race.print_status()