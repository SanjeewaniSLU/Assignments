
#1
class car():
    def __init__(self,r,m,c,t):
        self.registration_number = r
        self.maximum_speed = m
        self.current_speed = c
        self.travelled_distance = t

new_car =car("ABC-123","142 km/h","0","0")
print(f"Properties of the new car:-\nRegistarion number-",new_car.registration_number,"\nMaximum speed-",
      new_car.maximum_speed,"\nCurrent Speed-",new_car.current_speed,"km/h\nTravelled Distance-",
      new_car.travelled_distance,"km")

#2
