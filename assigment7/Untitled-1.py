print("---TASK 1---")
class Car:
    def __init__(self, reg_number, max_speed):
        self.registration_number = reg_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

car = Car("ABC-123", 142)

print("Registration number:", car.registration_number)
print("Max speed:", car.max_speed)
print("Current speed:", car.current_speed)
print("Travelled distance:", car.travelled_distance)



print("---TASK 2---")
class Car:
    def __init__(self, reg_number, max_speed):
        self.registration_number = reg_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        self.current_speed += change

        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed

        if self.current_speed < 0:
            self.current_speed = 0

car = Car("ABC-123", 142)

car.accelerate(30)
car.accelerate(70)
car.accelerate(50)
print("Current speed:", car.current_speed)
car.accelerate(-200)
print("Final speed:", car.current_speed)



print("---TASK 3---")
class Car:
    def __init__(self, reg_number, max_speed):
        self.registration_number = reg_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        self.current_speed += change

        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed

        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours
car = Car("ABC-123", 142)

car.current_speed = 60
car.travelled_distance = 2000
car.drive(1.5)
print("Travelled distance:", car.travelled_distance)