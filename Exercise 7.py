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
