print ("Hello! This is your petrol consumption calculator!\n")
miles = float(input("How many miles have you driven?\n"))
avgMPG = float(input("How many miles per gallon does your car get?\n"))
petrolCost = float(input("How much does petrol cost per litre?\n"))
journeyCost = (miles/(avgMPG/4.54609))*petrolCost 
print ("Your journey cost is £",round(journeyCost, 3))