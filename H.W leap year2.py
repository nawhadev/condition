year= int(input("Enter a year:"))
if year % 400 == 0:
    print("It is a Leap year!")
elif year % 100 == 0:
    print("It is NOT a Leap year!")
elif year % 4 == 0:
    print("It is a Leap year!")
else:
    print("It is NOT a Leap year!")
