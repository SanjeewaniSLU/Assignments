
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

    def drive(self,new_distance,new_speed, hours):
        self.travelled_distance = new_distance + (new_speed * hours)
        self.new_distance = new_distance
        self.new_speed = new_speed
        self.hours = hours


my_car = Car("ABC-123", 142)


print(f"Registration Number:",my_car.registration_number,"\nMaximum Speed:",my_car.max_speed," km/h. \nCurrent Speed:",my_car.current_speed," km/h\nTravelled Distance:",my_car.travelled_distance,"km")


my_car.accelerate(30)
print(f"Current Speed after acceleration:",my_car.current_speed," km/h")
my_car.accelerate(70)
print(f"Current Speed after acceleration:",my_car.current_speed," km/h")
my_car.accelerate(50)
print(f"Current Speed after acceleration:",my_car.current_speed," km/h")

my_car.accelerate(-200)
print(f"Final Speed after emergency brake:",my_car.current_speed," km/h")


my_car.drive(2000,60,1.5)
print(f"New Travelled Distance:",my_car.travelled_distance,"km")
