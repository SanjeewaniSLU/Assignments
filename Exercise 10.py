# -1
class Elevator:
    def __init__(self,top_floor, bottom_floor):
        self.top_floor = top_floor
        self.bottom_floor = bottom_floor
        self.current = self.bottom_floor

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
    def __init__(self, no_top, no_bottom, no_elevators):
        self.no_top = no_top
        self.no_bottom = no_bottom
        self.no_elevator = no_elevators
        self.list_elevators = []
        for num in range(0,no_elevators):
            elevator = Elevator(self.top_floor,self.bottom_floor)
            self.list_elevators.append(elevator)

    def run_elevator(self,no_elevator,des_floor):
        if no_elevator in self.list_elevators:
            print(f" Elevator number,{[no_elevator-1]} go to the floor{des_floor}")
            h.go_to_floor(des_floor)
        else:
            print(f"No of elevator is wrong.")


b = Building(10,1,3)
print(f"These are the elevators in building 1,{b.list_elevators}")

# -3
    def fire_alarm(self):
        print("There is a fire alarm in your building. All elevators go down")
        h.go_to_floor(0)

b.fire_alarm()







