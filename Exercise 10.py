# -1


class Elevator:
    def __init__(self,top_floor, bottom_floor):
        self.top_floor = top_floor
        self.bottom_floor = bottom_floor
        self.current = bottom_floor

    def floor_up(self):
        if self.current < self.top_floor:
            self.current += 1
            print(f" Now the floor number is {self.current}")

    def floor_down(self):
        if self.current > 0:
            self.current -= 1
            print(f" Now the floor number is {self.current}")

    def go_to_floor(self, floor):
        while self.current < floor:
            self.floor_up()
        while self.current > floor:
            self.floor_down()


h = Elevator(10, 0)
h.go_to_floor(5)
h.go_to_floor(0)

#-2


class Building:
    def __init__(self, top_floor, bottom_floor, elevators):
        self.top_floor = top_floor
        self.bottom_floor = bottom_floor
        self.elevators = elevators
        self.list_elevators = []
        for num in range(0, elevators):
            elevator = Elevator(self.top_floor, self.bottom_floor)
            self.list_elevators.append(elevator)

    def run_elevator(self, no_elevator, des_floor):
        if no_elevator < len(self.list_elevators):
            print(f"Elevator number {no_elevator} go to the floor {des_floor}")
            self.list_elevators[no_elevator].go_to_floor(des_floor)
        else:
            print("No such elevator.")

# -3

    def fire_alarm(self):
        print("Fire alarm!!!.All elevators move to down.")
        h.go_to_floor(0)

#-2

b = Building(10,0,5)
b.run_elevator(1, 5)
b.run_elevator(2, 4)

#-3

b.fire_alarm()
h.go_to_floor()

#-4


class Car:
    def __init__(self,reg_no, max_speed):
        self.reg_no = reg_no
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0
        self.brake = -200

    def accelerate(self, change):
        new_speed = self.current_speed + change
        if new_speed < 0:
            self.current_speed = 0
        elif new_speed > self.max_speed:
            self.current_speed = self.max_speed
        else:
            self.current_speed = new_speed

    def drive(self, hours):
        distance = self.current_speed * hours
        self.travelled_distance += distance


class Race:
    def __init__(self, name, distance_km, car):
        self.name = name
        self.distance_km = distance_km
        self.car = car


    def hour_passes(self):
        for car in self.car:
            car.accelerate(random.randint(-15, 10))
            car.drive(1)

    def print_status(self):
        print("-" * 60)
        print(f"Race: {self.name} | Distance: {self.distance_km} km")
        print("{:<15} {:<15} {:<15} {:<15} {:<15}".format("Car", "Max Speed (km/h)", "Current Speed (km/h)",
                                                          "Distance Traveled (km)", "Status"))
        for car in self.car:
            status = "Finished" if car.travelled_distance >= self.distance_km else "In Progress"
            print("{:<15} {:<15} {:<15} {:<15} {:<15}".format(car.reg_no, car.max_speed,
                                                              car.current_speed, car.travelled_distance, status))
        print("-" * 60)

    def race_finished(self):
        return any(car.travelled_distance >= self.distance_km for car in self.car)

new_car = Car("ABC-123", 142)


import random
car = []

for i in range(1, 11):
    reg_no = f"ABC-{i}"
    max_speed = random.randint(100,200)
    car_number = Car(reg_no, max_speed)
    car.append(car_number)

grand_derby = Race("Grand Demolition Derby", 8000, car)

hours = 0
while not grand_derby.race_finished():
    grand_derby.hour_passes()
    if hours % 10 == 0:
        grand_derby.print_status()
    hours += 1

grand_derby.print_status()
print("Race finished after", hours,"hours.")










