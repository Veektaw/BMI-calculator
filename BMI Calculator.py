weight = int(input("Enter your weight: "))
height = float(input("Enter your height: "))

BMI = weight / (height * height)
if BMI < 18.5:
    print("Underweight")
elif BMI >= 18.5 and BMI < 24.9:
    print("Normal weight")
elif BMI >= 25 and BMI < 29.9:
    print("Overweight")
else:
    print("Obese")