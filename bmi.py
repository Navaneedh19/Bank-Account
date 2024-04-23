#BMI Code
height = input()
weight = input()

height_as_float = float(height)
weight_as_int = int(weight)

bmi = weight_as_int / height_as_float ** 2
bmi_as_int = bmi
print(round(bmi))