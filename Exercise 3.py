
#1

z =float (input("Length of a zander in cms: "))
if z>=42:
    print("Zander fulfills the required length. " )
else:
    print(f"Release the zander into tank.It's {42-z}cms below the required length.")


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


 #3

gender = input("Enter your biological gender:")
hemoglobin_level = float(input("Enter your hemoglobin_level in g/l:"))
if gender == 'female':
    if hemoglobin_level < 117:
        print("Your hemoglobin level is low.")
    elif 117 <= hemoglobin_level <= 155:
        print("Your hemoglobin level is normal.")
    elif hemoglobin_level > 155:
        print("Your hemoglobin level is high.")

elif gender == 'male':
    if hemoglobin_level < 134:
        print("Your hemoglobin level is low.")
    elif 134 <= hemoglobin_level <= 167:
        print("Your hemoglobin level is normal.")
    elif hemoglobin_level > 167:
        print("Your hemoglobin level is high.")
else:
    print("Enter correct data again.")



#4

year = int(input("Enter a year:"))
if year % 400 == 0 and year % 100 == 0:
    print("Entered year is a leap year.")
elif year % 4 == 0 and year % 100 != 0:
    print("Entered year is a leap year.")
else:
    print("Entered year is not a leap year.")



