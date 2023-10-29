# -1
class Elevator:
    def __init__(self,top_floor,bottom_floor):
        self.top = top_floor
        self.bottom = bottom_floor
        self.current = self.bottom

    def floor_up(self):
        if self.current < self.top:
            self.current += 1
            print(f" Now the floor number is {self.current}")

    def floor_down(self):
        if self.current > 0:
            self.current -= 1
            print(f" Now the floor number is {self.current}")

    def go_to_floor(self,floor):
        while self.current < floor:
            h.floor_up()
        while self.current > floor:
            h.floor_down()


h = Elevator(10,0,)
h.go_to_floor(5)
h.go_to_floor(0)


