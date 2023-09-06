#1
"""
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
        print("Exiting the program.")
        break

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
"""
   number = float(input("Enter a number or space:"))


      while number == " ":
      break

