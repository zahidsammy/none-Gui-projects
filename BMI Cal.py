# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = round(weight/height**2)

if BMI < 18.5:
    print(f"Your are Under Weight {BMI}")
    
elif BMI < 25:
    print(f"you are normal Weight {BMI}")

elif BMI < 30:
    print(f"you are Over weight {BMI}")

elif BMI < 35:
    print(f"You are obese {BMI}")

else:
    print(f"you are clinically Obese {BMI}")
    