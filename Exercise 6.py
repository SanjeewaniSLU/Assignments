#1
"""
import random

def dice_roll():
    return random.randint(1,6)


while True:
    result = dice_roll()
    print(f"You rolled the dice ,{result}")
    if result == 6:
        break

#2


def dice_roll(num_sides_dice):
    return random.randint(1,num_sides_dice)


num_sides_dice = int(input("Enter the number of sides on the dice: "))

while True:
    result = dice_roll(num_sides_dice)
    print(f"You rolled the dice, {result}")
    if result == num_sides_dice:
        break

#3

def gal_to_liters(gallons):
    liters = gallons * 3.7854
    return liters

while True:
    gallons = int(input("The number of gallons with gasoline in American : "))
    if gallons < 0:
        break

    liters = gal_to_liters(gallons)
    print(f"{gallons} American gasoline gallons are approximately {liters:.2f} liters.")

#4

def sum_of_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

numbers = [4, 5, 1, 6, 7]
result = sum_of_list(numbers)
print(f"The sum of the numbers in the list is: {result}")


#5
new_list = []

def get_list (numbers):
    for i in numbers:
        if i % 2 == 0:
            new_list.append(i)

original_list = [4, 5, 1, 6, 7]
get_list(original_list)
print(original_list)
print(new_list)

"""
