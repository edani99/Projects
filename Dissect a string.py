print("Welcome to Dissect that String!\n")

#make a variable (any name) that asks the user for a string
user_string = input("Enter a string: ")

#on the other side of the plus sign, write the code that returns the length of the string that the user inputted
print("Word Count: " + str(len(user_string)))

#on the other side of the plus sign, write the code that returns the string in uppercase
print("In upper case: " + user_string.upper())

#on the other side of the plus sign, write the code that returns the string in lowercase
print("In lower case: " + user_string.lower())

#on the other side of the plus sign, write the code that returns the 1st letter of the string (hint: index position 0)
print("The first letter of the string is: " + user_string[0])

#on the other side of the plus sign, write the code that returns the last letter of the string (hint: this would be at index position of the strings length minus 1)
print("The last letter of the string is: " + user_string[-1])