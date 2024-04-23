print("Welcome to the roller coaster.")
bill = 0
height = int(input("What is your height in cm?\n"))
if height >= 120:
    print("You can ride.")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <=18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        age >= 18
        bill = 12
        print("Adults tickets are $12.") 
    want_photo = input("Do you want to take photo? Y or N")
    if want_photo == "Y":
        bill+= 3
        print(f"Your final bill is ${bill}.")
else:
    print("You can't ride.")    
