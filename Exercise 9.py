
#1
class car():
    def __init__(self,r,m,c,t):
        self.Registration_number = r
        self.Maximum_speed = m
        self.Current_speed = c
        self.Travelled_distance = t


new_car =car("ABC-123","142 km","0","0")
print(f"Properties of the new car:-\nRegistarion number",new_car.Registration_number,"\nMaximum speed-",new_car.Maximum_speed,"\nCurrent Speed-",new_car.Current_speed,"\nTravelled Distance-",new_car.Travelled_distance)
# class pet():
#     counter = 0
#
#     def __init__(self,n,c):
#         self.fName = n
#         self.color = c
#         pet.counter += 1
#
#     def bark(self,n):
#         for i in  range(n):
#             print("Bark,Bark")
#
#     def setName(self,n):
#         self.fName = n
#         print ("Name is changed")
#
#     def getColor(self):
#         return self.color
#
# dog = pet("Snowy","White")
# cat = pet("Chick","Grey")
# snake = pet("Python","Yellow")
#
# print(dog.fName,dog.color)
# print(cat.fName,cat.color)
# print(snake.fName,snake.color)
#
# dog.bark(5)
# print("My snake also bark,see")
# snake.bark(2)
#
# dog.setName("Bow")
# print(dog.fName)
# print(f"Here is the dog color",dog.getColor())
# print("Number of objects", pet.counter)