import math

print("Welcome to the Calculator!")

x = int(input("Enter a number: "))
y = int(input("Enter another number: "))
print(f"Total: {x + y}")

x = int(input("Enter a number: "))
y = int(input("Enter another number: "))
print(f"Difference: {x - y}")

x = int(input("Enter a number: "))
y = int(input("Enter another number: "))
print(f"Product: {x * y}")

x = int(input("Enter a number: "))
y = int(input("Enter another number: "))
print(f"Quotient: {x / y}") 

x = int(input("Enter a number: "))
y = int(input("Enter another number: "))
print(f"Exponent: {math.pow(x, y)}")

x = int(input("Enter a number: "))
print(f"Absolute Value: {math.fabs(x)}")
x = int(input("Enter a number: "))
print(f"Square Root: {math.sqrt(x)}")