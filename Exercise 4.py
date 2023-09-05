#1
"""
number = 1
while number <= 1000:
    if number % 3 == 0:
        print(number)
    number += 1


#2
number = float(input("Enter a value in Inches:"))
while number < 0:
     print ("End")
     break
if number >= 0:
     cm = number * 2.54
     print(f"Entered value in cms :{cm:.2f}")
number = float(input("Enter a number or space:"))
while number == " ":
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

   number = float(input("Enter a number or space:"))


      while number == " ":
      break
"""
number = 0
while number >= 0:
    if number >= 0:
        cm = number*2.54
        number = float(input('Enter no: '))

    else:
        break
