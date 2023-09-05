"""
list=[]
while True:
    number = int(input("Enter a number:"))

    if number < 0:
        break
    list.append(number)
print("Numbers you have entered:")
print(list)

"""
shop=[]
while True:
    cart = input("What you bought from shop:")
    if cart == 'done':
        break
    else:
        shop.append(cart)
print("\n shopping list")
for index,item in enumerate(shop,start=1):
    print(f"{index}.{item}")