
#1
number = 1
while number <= 1000:
    if number % 3 == 0:
        print(number)
    number += 1


#2
while True:
    number = float(input('Enter a number: '))

    if number >= 0:
        cm = number * 2.54
        print(f"Entered value in cm: {cm:.2f}")
    else:
        print("End of the program.")
        break

#3
smallest_number = None
largest_number = None

while True:
    input_number = input("Enter a number or press Enter to quit:")
    if input_number == "":
        break

    number = float(input_number)

    if smallest_number is None or number < smallest_number:
        smallest_number = number

    if largest_number is None or number > largest_number:
        largest_number = number

if smallest_number is not None and largest_number is not None:
    print(f"Smallest number: {smallest_number}")
    print(f"Largest number: {largest_number}")


#4

import random
number_1 = random.randint(1 ,10)
Guess_number = 0
while Guess_number != number_1:
     Guess_number = int(input("Guess a number:"))
     if Guess_number < number_1:
      print("Too low!")
     elif Guess_number > number_1 :
      print("Too high!")
     else:
      print("Correct!!!")

#5

correct_username = "hello"
correct_password = "great"

tries = 0
while tries < 5:
   username = input("Enter your Username:")
   password = input("Enter your Password:")
   if username == correct_username and password == correct_password:
      print("Welcome!")
      break
   else:
      print("Incorrect username and password,Please try again.")
      tries += 1

if tries == 5:
    print("Access denied.")

#6


import random
#Total number of random points
N = int(input("Enter the number of points:"))

#Total number of points in square
m = 1
#Total number of points in cirlce
n = 0

while m <=N:
     x=random.uniform(-1,1)
     y=random.uniform(-1,1)
     if x ** 2 + y ** 2 <= 1:
         n += 1
     m = m + 1
pi = 4 * n / N
print(f"pi = {pi}")









