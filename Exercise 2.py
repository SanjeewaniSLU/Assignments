import math
#1.
name = input("What is your name?")
print(f"Hello,{name}!")

#2.
radius = float(input("Enter radius of the circle:"))
area = math.pi * radius ** 2
print(f"The area of the circle:{area:.2f}")

#3.
length = float(input("Enter the length of rectangle:"))
width = float(input("Enter the width of rectangle:"))
perimeter = (length + width) * 2
area = length*width
print(f"The perimeter of the rectangle:{perimeter:.2f}")
print(f"The area of the rectangle:{area:.2f}")

#4.
number1 =float(input("Enter one integer number:"))
number2 =float(input("Enter another integer number:"))
number3 =float(input("Enter one more integer number:"))
sum = number1 + number2 + number3
product = number1 * number2 * number3
average = sum / 3
print(f"sum of three integer numbers:{sum}")
print(f"product of three integer numbers:{product}")
print(f"average of three integer numbers:{average}")

#5.
talent_g = 20 * 32 * 13.3
pounds_g = 32 * 13.3
lots_g = 13.3

talents = int(input("Enter talents:\n"))
pounds = int(input("Enter pounds:\n"))
lots = float(input("Enter lots:\n"))

weight = (talents*talent_g) + (pounds*pounds_g) + (lots*lots_g)
print(f"The weight in modern units:\n{weight//1000} kilograms and {weight % 1000:.2f} grams.")

#6
import random

num1 = random.randint(0,9)
num2 = random.randint(0,9)
num3 = random.randint(0,9)
print(f'Your 3 digit code between 0-9 is: {num1}{num2}{num3}')

num4 = random.randint(1,6)
num5 = random.randint(1,6)
num6 = random.randint(1,6)
num7 = random.randint(1,6)
print(f'Your 4 digit code between 1-6 is: {num4}{num5}{num6}{num7}')