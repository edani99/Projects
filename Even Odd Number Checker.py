print("Even-Odd Number Checker\n")

choice = ""
while choice != "STOP":
  while True:
    try:
      user_number=int(input("Enter a number: "))
      break
    except ValueError:
      print("Invalid input. Please enter a number.")
  if user_number % 2 == 0:
    print(f"{user_number} is an even number.")
  else:
    print(f"{user_number} is an odd number.")


  choice = input("Do you still want to play? (Enter STOP to stop playing): ")
    #inside of a try block, ask the user for a number, and break from the       block after.
   

    #inside of the except block, check for a value error. If there is a         value error, the code inside of this block will run. The only code         that needs to run is a message stating that the user must enter a          number.


  #now outside of the while true loop, you need to check if the user's        number is even or odd. Remember, you must use the modulo (%) operator      to check if the user's number divided by 2 has a remainder of 0. If it     does, the number is even. Else, the number is not
