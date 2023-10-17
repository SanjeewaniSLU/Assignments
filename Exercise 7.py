#1

seasons = ('Winter', 'Spring', 'Summer', 'Autumn')

number_of_month = int(input("Enter the number of a month (1-12): "))


if 3 <= number_of_month <= 5:
    season = seasons[1]
elif 6 <= number_of_month <= 8:
    season = seasons[2]
elif 9 <= number_of_month <= 11:
    season = seasons[3]
elif number_of_month == 12 or number_of_month <= 2:
    season = seasons[0]
else:
    print("Invalid input. Please enter a number between 1 and 12.")
    exit()
print(f"The season for month {number_of_month} is {season}.")

#2
user_names_set = set()

while True:
    name = input("Enter a name or press 'Enter' to quit: ")
    if name == "":
        break
    if name in user_names_set:
        print("Existing name")
    else:
        print("New name")
        user_names_set.add(name)


print("\nList of input names:")
for name in user_names_set:
    print(name)

#3
airport_data = {}

while True:
    print("\nOptions:")
    print("1. Enter a new airport")
    print("2. Fetch airport information")
    print("3. Quit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        icao_code = input("Enter the ICAO code of the airport: ")
        airport_name = input("Enter the name of the airport: ")
        airport_data[icao_code] = airport_name

    elif choice == '2':
        icao_code = input("Enter the ICAO code of the airport: ")
        if icao_code in airport_data:
            print(f"The name of the airport is: {airport_data[icao_code]}")
        else:
            print("Airport not found.")

    elif choice == '3':
        break
