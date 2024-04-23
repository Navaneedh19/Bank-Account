#BMI Calculation using Nested if & Elif

height = float(input())
weight = int(input())

bmi = weight / height ** 2
if bmi<18.5:
    print (f"Your BMI is {bmi}. You are underweight.")
elif bmi<25:
    print(f"Your BMI is {bmi}. You are normal weight.")
elif bmi <30:
    print(f"Your BMI is {bmi}. You're slightly over weight.")
elif bmi<35:
    print(f"Your BMI is {bmi}. You are Obese.")
else:
    print (f"Your BMI is {bmi}. You are clinically obese.")        
