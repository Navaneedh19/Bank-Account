import random 

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8','9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
print("Welcome to the Password Generator!")

nr_letter = int(input("How many letters would you like in your password?\n"))
nr_number = int(input("How many number would you like in your password?\n"))
nr_symbol = int(input("how many symbols would you like in your pasword?\n"))

password =" "

for char in range(1, nr_letter+1):
    password += random.choice(letters)
for char in range(1, nr_number+1):
    password += random.choice(numbers)
for char in range(1, nr_symbol+1):
    password += random.choice(symbols)

print(password)
password_list = list(password)
random.shuffle(password_list)        
print(password_list)
password =" "
for char in password_list:
    password += char
print(f"Your Password is:{password}.")
if __name__ == "__main__":
