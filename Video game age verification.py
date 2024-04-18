print("Welcome to Video Game Age Verification!\n")

age = int(input("Enter your age to see what games you can play: "))

animalCrossing = False
superMario = False
roblox = False
fortnite = False
callOfDuty = False

if age>= 0 and age<=17:
  print("You are old enough")

if age>=0 and age<=17:
  print("You can play Animal Crossing")
  animalCrossing = True
else: 
  animalCrossing = False
 
if age>=10 and age<=17:
  print("You can play Super Mario Odyssey")
  superMario = True
else:
  superMario = False
 
if age>=12 and age<=17:
  print ("You can play Fortnite")
  fortnite = True
else: 
  fortnite = False
 
if age>=10 and age<=17:
  print("You can play Roblox")
  roblox = True
else:
  roblox = False
 
if age == 17:
  print( "You can play Call Of Duty")
  callOfDuty = True
else:
  callOfDuty = False

if animalCrossing and superMario and roblox and fortnite and callOfDuty == True:
  print("You are allowed to play every game")

else:
  if animalCrossing == True:
    print("You can play Animal Crossing")
  elif superMario == True:
    print("You can play Super Mario Odyssey")
  elif roblox == True:
    print("You can play Roblox")
  elif fortnite == True:
    print("You can play Fortnite")
         
    