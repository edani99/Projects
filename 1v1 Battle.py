print("Welcome to 1v1 battle\n")
choice = ""
player1Health = 1000
player2Health = 1000

player1 = input("Player 1, what is your name? ")
player2 = input("Player 2, what is your name? ")

while choice.lower() != "no":
 choice = ""
 
 damageToPlayer2 = input(player1 + ", how much damage do you want to do to " + player2 + "? ")

 
 player2Health = player2Health - int(damageToPlayer2)

 damageToPlayer1 = input(player2 + ", how much damage do you want to do to " + player1 + "? ") 


 player1Health = player1Health - int(damageToPlayer1)
 
 choice = input("Would you like to play again? (yes/no)")


totalDamageToPlayer1 = 1000 - player1Health
totalDamageToPlayer2 = 1000 - player2Health

print(f"In total, {player1} did {totalDamageToPlayer2} to {player2}")
print(f"In total, {player2} did {totalDamageToPlayer1} to {player1}")

if totalDamageToPlayer2 > totalDamageToPlayer1:
  print(f"{player1} wins!")

elif totalDamageToPlayer1 > totalDamageToPlayer2:
  print(f"{player2} wins!")

else:
  print("draw")


