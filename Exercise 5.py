#1
"""
import random

dices = int(input("How many dice to roll?"))
total_sum = 0

for dice in range(dices):
    roll = random.randint(1,6)
    print(f"Rolling a die:{roll}")
    total_sum += roll
print(f"Total sum of {dices} dices numbers: {total_sum}")

#2

number=[]

while True:
    input_number = input("Enter a number or press Enter to quit:")
    if input_number == "":
        break
    else:
        number.append(input_number)

if len(number) >= 5:
    number.sort(reverse=True)
    print("Five greatest numbers in descending order:")
    for i in range(5):
        print(number[i])


#3
number=[]

prime_number = number//1 and number//number

while True:
    integer = int(input("Enter an integer:"))
    if integer == prime_number:
        print("It's a prime number.")
    else:
        print(f"It's not a prime number.")

"""
#4
cities = []
for i in range(5):
    city = input(f"Enter the name of city {i + 1}:")
    cities.append(city)

print("Names of cities:")
for index,item in enumerate(cities,start=1):
    print(f"{index}.{item}")