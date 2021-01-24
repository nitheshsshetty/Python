import hangman_logo
import words
import hangman
import random
import os

# word_list = ["aardvark", "baboon", "camel"]
word_list = random.choice(words.word_list)
print(hangman_logo.hangman)
#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word= random.choice(words.word_list)
blank=[]
for i in range(len(chosen_word)):
   blank += "_"
#print('  '.join(blank))

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
i=0
wrdlen = len(chosen_word)
chosen_word = list(chosen_word)

life=6
first=0
not_found = 0
temp = []
while life > 0: 
  if first != 0:
   print(hangman.stages[life])
  guess=input("\n Guess the letter : ").lower()
  
  first = 1
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
  
  if guess in chosen_word:
       for i in range(wrdlen):
         if guess == chosen_word[i]:
           os.system('clear')
           blank[i] = guess
           not_found = 0
       temp.append(guess)      
  else:
     life -= 1
     os.system('clear')
     print(' '.join(blank))
     print(f"\nYou guessed {guess}, that's not in the word. You lose a life.")  
     not_found = 1
  
  if guess in temp: 
    count=1
    for k in range(len(temp)):
      if temp[k] == guess:
        count += 1
    if count > 2: 
     print(f"You've already guessed {guess}")
  
  if not_found == 0:
   print(' '.join(blank))

  if "_" not in blank:
    print("\n You have WON !")
  
  
   
 
print(hangman.stages[life])
print("\n You Lose")

