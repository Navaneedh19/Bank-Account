import os

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        else:
            return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False

    def check_balance(self):
        return self.balance

    def __str__(self):
        return f"Account Number: {self.account_number}\nBalance: {self.balance}"


def load_accounts(filename):
    accounts = {}
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            for line in file:
                try:
                    account_number, balance = line.strip().split(',')
                    accounts[account_number] = BankAccount(account_number, float(balance))
                except ValueError:
                    print(line.strip())
    return accounts


def save_accounts(accounts, filename):
    with open(filename, 'w') as file:
        for account_number, account in accounts.items():
            file.write(f"{account_number},{account.balance}\n")

def main():
    filename = "accounts.txt"
    accounts = load_accounts(filename)

    while True:
        print("\nWelcome to the Bank Account Management System")
        print("1. Create new account")
        print("2. Access existing account")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            account_number = input("Enter account number: ")
            if account_number not in accounts:
                accounts[account_number] = BankAccount(account_number)
                print("Account created successfully!")
            else:
                print("Account already exists!")

        elif choice == '2':
            account_number = input("Enter account number: ")
            if account_number in accounts:
                account = accounts[account_number]
                print(account)
                while True:
                    print("\n1. Deposit")
                    print("2. Withdraw")
                    print("3. Check Balance")
                    print("4. Go back")
                    option = input("Enter your choice: ")

                    if option == '1':
                        amount = float(input("Enter amount to deposit: "))
                        if account.deposit(amount):
                            print("Deposit successful!")
                        else:
                            print("Invalid amount!")

                    elif option == '2':
                        amount = float(input("Enter amount to withdraw: "))
                        if account.withdraw(amount):
                            print("Withdrawal successful!")
                        else:
                            print("Insufficient funds or invalid amount!")

                    elif option == '3':
                        print("Current Balance:", account.check_balance())

                    elif option == '4':
                        break

                    else:
                        print("Invalid option!")

            else:
                print("Account not found!")

        elif choice == '3':
            save_accounts(accounts, filename)
            print("Thank you for using the Bank Account Management System!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()



     

    
 

        




