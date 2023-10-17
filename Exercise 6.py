#1

import random

def dice_roll():
    return random.randint(1,6)


while True:
    result = dice_roll()
    print(f"You rolled the dice ,{result}")
    if result == 6:
        break

