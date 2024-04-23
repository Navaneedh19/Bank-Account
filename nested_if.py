#Nested if statement & Elif statement
print("Welcome to the Roller Coaster!")
height = int(input("What is you height in cm?\n"))
if height >= 120:
    print("You can ride")
    age = int(input("what is your age?\n"))
    if age<12:
        print("You have to pay $5.")
    elif age<=18:
        print("You have to pay $7.")
    elif age<=25:
        print("You have to pay $10.")    
else:
    print("Sorry you have to grow taller.")    