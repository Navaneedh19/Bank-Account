print("Welcome to the Treasure Island.")
print("Your mission is to find the Treasure.")
choice1 = input('You\'re at a cross road, where do you want to go? Type "left" or "right".\n').lower()
if choice1 == "left":
   choice2 = input('You\'re come to lake. There is an island in the middle of the lake. Type "Wait" to wait for a boat or type "Swim" to swim across.\n').lower()
   if choice2 == "wait":
      choice3 = input('You arrived at the island. There is a house with 3 doors. One red, one yellow, one blue. Which colour do you choose?.\n').lower()
      if choice3 == "red":
          print("It's a room full of fire. Game Over")
      elif choice3 == "yellow":
         print("You found a treasure! You win!.")
      elif choice3 == "blue":
         print("You entered a room of beast.Game Over.")
      else:
         print ("you choose a door that doesn't exist. Game Over") 
   else:
      print("Game Over")
else:
   print("You fell into a hole. Game Over.")

      