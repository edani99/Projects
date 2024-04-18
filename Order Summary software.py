price = 0
print("Welcome to Pizza Paradise!\n")

print("\nAvailable Pizza Sizes:")
print("1. Small ($10) \n2. Medium ($15) \n3. Large ($20)")

size = int(input("What size pizza would you like? (1, 2, or 3) "))

if size > 3 or size < 1:
  print("Invalid size. Please try again.")
 
else:
  if size == 1:
    price = price + 10
  elif size == 2:
    price = price + 15
  elif size == 3:
    price = price + 20
print("\nAvailable Pizza Toppings:")
print(
    "1. Pepperoni ($2) \n2. Mushrooms ($1.50) \n3. Onions ($1) \n4. Extra Cheese ($1.75)")


topping = int(input("What topping would you like? (1, 2, 3, or 4)"))

if topping > 4 or topping < 1:
                    print(
                        "Invalid topping. Please try again.")

else:
   if topping == 1:        price = price + 2
   elif topping == 2:      price = price + 1.5  
   elif topping == 3:      price = price + 1
   elif topping == 4:      price = price + 1.75
print("\nAvailable Drinks:")
print("1. Soda ($2) \n2. Water ($1)")

drink = int(input("What drink would you like? (1 or 2)"))

if drink > 2 or drink < 1:
                    print("Invalid drink. Please try again.")

else:
   if drink == 1:        price = price + 2
   elif drink == 2:      price = price + 1

print("-------------------------------\n")
print("Order Summary:")
print(f"Pizza Size: {size}")
print(f"Topping: {topping}")
print(f"Drink: {drink}")
print("Total Cost: ${:.2f}".format(price))