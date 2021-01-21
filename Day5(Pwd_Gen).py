#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("\n---------------- Welcome to the PyPassword Generator -------------------\n")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
letter1=""

# print(type(letter1))
for i in range(nr_letters):
 letter1=letter1+random.choice(letters)
for i in range(nr_symbols):
 letter1=letter1+random.choice(symbols)
for i in range(nr_numbers):
 letter1=letter1+random.choice(numbers)

print(f"\n= = = = = = = = = Eazy Level = = = = = = = = =\n\nRandom number generated is : {letter1}") 
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

letter2= ""
letter2=''.join(random.sample(letter1,len(letter1)))
print(f"\n\n= = = = = = = = = Hard Level = = = = = = = = =\n\nRandom number generated is : {letter2}") 

print("\n\n======================== Thank you for Using ===============================")
