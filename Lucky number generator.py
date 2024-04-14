
import math  
import random
print("Welcome to the lucky number generator!\n")
fName = input("Please provide your name: ")
lName = input("Please provide your last name: ")
age = int(input("Please provide your age: "))
x = len(fName +lName)
y = random.randint(1,100)
luckyNum = math.ceil(x + y + age)
print("Your lucky number is: " + str(luckyNum))
