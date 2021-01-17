
print("--------- WELCOME TO SPILT-IT --------")
bill=float(input("\nEnter the total bill amount : "))
tip=int(input("\nEnter the tip (10% ,12% ,15%) : "))
count=int(input("\nEnter the people count : "))
total_bill = round(float(bill + (bill*(tip/100)))/count,2)
total_bill="{:.2f}".format(total_bill)
print(f"\nAmount to be paid by each individual : ${total_bill}")
