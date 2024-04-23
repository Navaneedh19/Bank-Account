def division ():
   try:
        dividend = float(input("Enter the dividend: "))
        divisor = float(input("Enter the divisor: "))
        result = dividend / divisor
        print(f"Result of division: {result}")

   except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
    
   except ValueError:
        print("Error: Please enter a valid numerical inputs.")

division()


