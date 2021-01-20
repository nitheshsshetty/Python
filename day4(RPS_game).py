import random 
#Python illustration of RPS(Rock Paper Scissor) game[you vs computer]

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game=[rock,paper,scissors]

user = int(input("What do you choose \n Type 0 for ROCK \n Type 1 for PAPER \n Type 2 for SCISSORS \n  "))

print(f"\n Your Choice is :\n {game[user]} ")
rand=[0,1,2]
computer = random.choice(rand)
print(f"\n Computer Choice is :\n {game[computer]} ")
  
if user == 0 and computer == 1:
  print("\nPaper Wraps Rock.. \n  Computer WON !!")
elif user == 0 and computer == 2:
  print("\nRock Crushes Scissors..\n You WON !!")
elif user == 0 and computer == 0:
  print("\n Rock faces Rock..\n Nobody WON !!")
elif user == 1 and computer == 1:
  print("\nPaper faces paper..\n Nobody WON !!")
elif user == 1 and computer == 2:
  print("\n Scissors cut Paper..\n Computer WON !!")
elif user == 1 and computer == 0:
  print("\n Paper wraps Rock..\n You WON !!")
elif user == 2 and computer == 1:
  print("Scissors cut Paper.. \n You WON !!")
elif user == 2 and computer == 2:
  print("\n scissors face scissors..\n Nobody WON !!")
else:
  print("\nRock crushes Scissors..\n Computer WON !!")
