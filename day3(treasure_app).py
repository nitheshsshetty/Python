print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

input1=input('\n You\'re at a cross road.Where do you want to go ?Type "left" or "right" ').lower()

if not input1 == 'right':
  input2=input('\n You come to a lake. There is an island in the middle of the lake, \n Type "wait" for a boat. Type "swim" to swim across >>').lower()
  if not input2 == 'swim':
    input3=input('\nYou arrive at the island unharmed.There is a house with 3 doors.\nOne Which door you want to select One Red ,one Blue and one yellow.\nWhich color do you choose?').lower()
    if input3 == "red":
      print("Burned by fire \n GAME OVER !!! ")
    elif input3 == "blue":
      print("\n Eaten by beasts.\n  GAME OVER !!! ")
    elif input3 == "yellow":
      print("\n YOU WIN !!!!!!")
    else:
      print("YOU LOSE !!!!!!")
  else :
    print("\n Attacked by trout. GAME OVER !!!")    
else :
  print("\nFall into a hole.\n GAME OVER !!!")
