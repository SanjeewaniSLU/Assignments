class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        new_speed = self.current_speed + change
        if new_speed < 0:
            self.current_speed = 0
        elif new_speed > self.max_speed:
            self.current_speed = self.max_speed
        else:
            self.current_speed = new_speed

    def drive(self, hours):
        self.travelled_distance = self.current_speed * hours


my_car = Car("ABC-123", 142)

print(f"Properties of the new car:\n\nRegistration Number:", my_car.registration_number,
      "\nMaximum Speed:", my_car.max_speed, " km/h."
                                            " \nCurrent Speed:", my_car.current_speed, " km/h\nTravelled Distance:",
      my_car.travelled_distance, "km")

my_car.accelerate(30)
print(f"Current Speed after acceleration:", my_car.current_speed, " km/h")
my_car.accelerate(70)
print(f"Current Speed after acceleration:", my_car.current_speed, " km/h")
my_car.accelerate(50)
print(f"Current Speed after acceleration:", my_car.current_speed, " km/h")

my_car.accelerate(-200)
print(f"Final Speed after emergency brake:", my_car.current_speed, " km/h")

my_car.accelerate(60)
my_car.drive(1.5)
print(f"New Travelled Distance:", my_car.travelled_distance, "km")

import random


class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0


cars = []


def random_speed():
    return random.randint(100, 200)


for i in range(1, 11):
    registration_number = f"ABC-{i}"
    maximum_speed = random_speed()
    new_car = Car(registration_number, maximum_speed)
    cars.append(new_car)

for car in cars:
    print(f"Registration Number:", car.registration_number)
    print(f"Maximum Speed:", car.max_speed, " km/h")
    print(f"Current Speed:", car.current_speed, " km/h")
    print(f"Travelled Distance:", car.travelled_distance, " km")
    print("-" * 30)


    def accelerate(self, change):
        change = random.randint(-15, 10)
        new_speed = self.current_speed + change
        if new_speed < 0:
            self.current_speed = 0
        elif new_speed > self.max_speed:
            self.current_speed = self.max_speed
        else:
            self.current_speed = new_speed


    def drive(self, hours):
        self.travelled_distance = self.current_speed * hours

car.travelled_distance(10000)
car.drive(1)