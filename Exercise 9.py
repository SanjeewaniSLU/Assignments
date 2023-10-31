# -1
class Car:
    def __init__(self,reg_no, max_speed):
        self.reg_no = reg_no
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0
        self.brake = -200
# -2

    def accelerate(self, change):
        new_speed = self.current_speed + change
        if new_speed < 0:
            self.current_speed = 0
        elif new_speed > self.max_speed:
            self.current_speed = self.max_speed
        else:
            self.current_speed = new_speed
# -3

    def drive(self, hours):
        distance = self.current_speed * hours
        self.travelled_distance += distance


my_car = Car("ABC-123", 142)

print(f"Properties of the new car:\n\nRegistration Number:", my_car.reg_no,
      "\nMaximum Speed:", my_car.max_speed, " km/h.""\nCurrent Speed:", my_car.current_speed, " km/h\nTravelled Distance:",
      my_car.travelled_distance, "km")

my_car.accelerate(30)
print(f"Current Speed after acceleration:", my_car.current_speed, " km/h")
my_car.accelerate(70)
print(f"Current Speed after acceleration:", my_car.current_speed, " km/h")
my_car.accelerate(50)
print(f"Current Speed after acceleration:", my_car.current_speed, " km/h")


my_car.brake
print(f"Final Speed after emergency brake:", my_car.current_speed, " km/h")

# my_car.accelerate(60)
my_car.drive(1.5)
print(f"New Travelled Distance:", my_car.travelled_distance, "km")

# -4

import random

cars = []

for i in range(1, 11):
    registration_number = f"ABC-{i}"
    maximum_speed = random.randint(100, 200)
    new_car = Car(registration_number, maximum_speed)
    cars.append(new_car)

no_hours = 0

while True:
    win_match = False
    for car in cars:
        car.accelerate(random.randint(-10, 15))
        car.drive(1)
        if car.travelled_distance >= 10000:
            win_match = True
            break
        no_hours += 1

    if win_match == True:
        break

print("-.-" * 15)
print("   The properties of 10 cars of the race.")
print("-.-" * 15)
for car in cars:
    print(f"Registration Number:", car.reg_no)
    print(f"Maximum Speed:", car.max_speed, " km/h")
    print(f"Current Speed:", car.current_speed, " km/h")
    print(f"Travelled Distance:", car.travelled_distance, " km")
    print("-" * 30)




