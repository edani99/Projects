print("Welcome to your Letter Grade Calculator\n")

math = float(input("What's your grade in Math: "))
science = float(input("What's your grade in Science: "))
english = float(input("What's your grade in English: "))
history = float(input("What's your grade in History: "))
worldLanguage = float(input("What's your grade in World Language: "))
physicalEducation = float(input("What's your grade in Physical Education: ")) 
averageGrade = math + science + english + history + worldLanguage + physicalEducation / 6
if averageGrade >= 90:
  print("Your average grade is an A")
elif averageGrade >= 80:
  print("Your average grade is a B")
elif averageGrade >= 70:
  print("Your average grade is a C")
elif averageGrade >= 60:
  print("Your average grade is a D")
else: 
  print("Your average grade is an F")
if averageGrade >= 70:
  print("You can play sports")