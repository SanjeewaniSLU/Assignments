
#1
"""
z =float (input("Length of a zander in cm"))
if z>=42:
    print("Zander fulfills the required length. " )
else:
    print(f"Release the zander into tank.It's {42-z}cm below the required length.")

"""
#2

cabin_class = input("Enter the cabin class of cruise ship : ")
if cabin_class == 'LUX':
    print("upper-deck cabin with a balcony.")
elif cabin_class == 'A':
    print("above the car deck, equipped with a window.")
elif cabin_class == 'B':
    print("windowless cabin above the car deck.")
elif cabin_class == 'C':
    print("windowless cabin below the car deck.")
else:
    print("Invalid cabin class.")