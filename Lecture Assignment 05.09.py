list=[]
while True:
    number = int(input("Enter a number:"))

    if number < 0:
        break
    list.append(number)
print("Numbers you have entered:")
print(list)
