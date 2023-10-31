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

#2

b = Building(10,0,5)
print(f"list of elevators.{b.list_elevators}")
b.run_elevator(1, 5)
b.run_elevator(2, 4)

#3

b.fire_alarm()











