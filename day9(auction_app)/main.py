from replit import clear
import art
#HINT: You can call clear() to clear the output in the console.


print(art.logo)
bid_details = {}
def bidders(name,bid):
  bid_details[name] = bid
  
max = 0
bidder=''
print("Welcome to the secret auction program")
proceed = "yes"
while proceed == "yes":
    name=input("What is ypur name ?:")
    bid=int(input("What is your bid? :"))
    bidders(name,bid)
    proceed = input("Are ther any bidder ?:").lower()
    clear()
clear()
for person in bid_details:
  if bid_details[person]> max:
    max = bid_details[person]
    bidder = person
print(f"Bid Winner is {bidder} with bid amounts to {max}")

