import math
#1.
#name = input("What is your name?")
#print(f"Hello,{name}")

#2.
#radius = float(input("Enter radius of the circle:"))
#area = math.pi * radius **2
#print(f"The are of the circle:{area:.2f}")

#3.
#length = float(input("Enter the length of rectangle:"))
#width = float(input("Enter the width of rectangle:"))
#perimeter = (length + width) * 2
#area = length*width
#print(f"The perimeter of the rectangle:{perimeter:.2f}")
#print(f"The area of the rectangle:{area:.2f}")

#4.
#number1 =float(input("Enter one integer number:"))
#number2 =float(input("Enter another integer number:"))
#number3 =float(input("Enter one more integer number:"))
#sum = number1 + number2 + number3
#product = number1 * number2 * number3
#average = sum / 3
#print(f"sum of three integer numbers:{sum}")
#print(f"product of three integer numbers:{product}")
#print(f"average of three integer numbers:{average}")

#5.
talents = float(input("Enter talents:"))
pounds = float(input("Enter pounds:"))
lots = float(input("Enter lots:"))

talents_g = 20 * 32 * 13.3 * talents
pounds_g = 32 * 13.3 * pounds
lots_g = 13.3 * lots

mass = talents_g + pounds_g + lots_g
mass_kg = mass // 1000
mass_g = mass % 1000
mass_kg_int = int(mass_kg)
print(f"The weight in modern units: \n {mass_kg_int} kilograms and {mass_g:.2f} grams.")


