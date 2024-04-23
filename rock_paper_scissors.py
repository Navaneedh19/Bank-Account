rock = """"
                                        
 8b,dPPYba,  ,adPPYba,   ,adPPYba, 88   ,d8   
 8 8P'   "Y8 a8"     "8a a8"     "" 88 ,a8"    
 88         8b       d8 8b         8888[      
 88         "8a,   ,a8" "8a,   ,aa 88`"Yba,   
 88          `"YbbdP"'   `"Ybbd8"' 88   `Y8a  
                                             
 """

paper = """"
                                                         
8b,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYba, 8b,dPPYba,  
88P'    "8a ""     `Y8 88P'    "8a a8P_____88 88P'   "Y8  
88       d8 ,adPPPPP88 88       d8 8PP""""""" 88          
88b,   ,a8" 88,    ,88 88b,   ,a8" "8b,   ,aa 88          
88`YbbdP"'  `"8bbdP"Y8 88`YbbdP"'   `"Ybbd8"' 88          
88                     88                                 
88                     88                                 

"""
import random
scissor = """"
                                                                             
,adPPYba,  ,adPPYba, 88 ,adPPYba, ,adPPYba,  ,adPPYba,  8b,dPPYba, ,adPPYba,  
I8[    "" a8"     "" 88 I8[    "" I8[    "" a8"     "8a 88P'   "Y8 I8[    ""  
 `"Y8ba,  8b         88  `"Y8ba,   `"Y8ba,  8b       d8 88          `"Y8ba,   
aa    ]8I "8a,   ,aa 88 aa    ]8I aa    ]8I "8a,   ,a8" 88         aa    ]8I  
`"YbbdP"'  `"Ybbd8"' 88 `"YbbdP"' `"YbbdP"'  `"YbbdP"'  88         `"YbbdP"'  

"""
import random
game_images = [rock, paper, scissor]
user_choice = int(input("what do you choose? Type 0 for rock, 1 for paper and 2 for scissor\n"))
if user_choice >= 3 or user_choice < 0:
  print("You typed an invalid number, You Lose!.")
else:
  print(game_images[user_choice])
  computer_choice = random.randint(0,2)
  print ("Computer Chose:") 
  print(game_images[computer_choice])

if user_choice == 0 and computer_choice == 2:
  print("You Win!.")
elif computer_choice == 0 and user_choice == 2:
  print("You Lose!.")
elif user_choice > computer_choice:
  print("You Win!.")     
elif computer_choice > user_choice:
  print("you Lose!.")
elif user_choice == computer_choice:
  print("It's a draw.")

