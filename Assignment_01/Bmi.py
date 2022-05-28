height = float(input("Enter your height (meters) : "))
weight = float(input("Enter your weight (kg) : "))

bmi = weight / (height**2)

if bmi < 18.5:
    print("Your BMI : ", bmi, "\n\n underweight.")

elif bmi >= 18.5 and bmi <= 24.9:
    print("Your BMI : ", bmi, "\n\n\tnormal.")

elif bmi >= 25 and bmi <= 29.9:
    print("your BMI : ", bmi, "\n\n\toverweight.")

elif bmi >= 30 and bmi <= 34.9:
    print("Your BMI : ", bmi, "\n\n\tobese.")

else:
    print("Your BMI : ", bmi, "\n\n\extremely obese.")
