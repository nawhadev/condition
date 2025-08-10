weight = float(input("Enter the weight in kg:"))
height = float(input("Enter the height in metre:"))
bmi = weight/height **2
print(f"Your Bmi is {bmi:0.2f}")

if bmi < 18.5:
    print("You are under weight!.Please gain some weight!")
elif 18.5 <= bmi <= 24.9:
    print("Your weight is normal!.Keep it up!")
elif 25 <= bmi <= 29.9:
    print("You are over weight!.Lose some weight!")
elif 30 <= bmi <= 34.9:
    print("you are obese!.losing weight is emergency!") 
else:
    print("You are extremely obese!.Visit the doctor as soon as possible!")
