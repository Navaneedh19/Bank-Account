print ("Thank you for choosing 'Navanee Pizza'.")
size = input("What size do you want? 'S','M', 'L'.")
bill = 0
if size == 'S':
    bill += 15
elif size == 'M':
    bill += 20
else:
    bill +=25
add_pepperoni = input("Do you want pepperoni? 'Y' or 'N'")
if add_pepperoni == 'Y':
    if size == 'S':
            bill += 2
    else:
            bill += 3
extra_cheese = input("Do you want extra cheese? 'Y' or 'N'")
if extra_cheese == 'Y':
    bill += 1
    print(f"Your final bill is ${bill}.")  
else:
     print(f"Your final bill is ${bill}.")              
