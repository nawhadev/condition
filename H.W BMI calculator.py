weight = int(input("Enter the weight in kg:"))
height = int(input("Enter the height in metre:"))
bmi = weight/height **2
print(f"Your bmi is {bmi:0.02f}")

if bmi <= 18.5:
    print("You are under weight.Please gain some weight!.")
elif 18.5 <= bmi <= 24.9:
    print("You are normal.Keep it up!.")
elif 24.9 <= bmi <= 24.9:
    print("You are over weight.Please lose some weight!.")
elif 30 <= bmi <= 34.9:
    print("You are obese.Losing weightbis emergency!.")
else:
    print("You are extreamely obese.Losing weight is emergency!.")