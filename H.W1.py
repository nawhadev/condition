year = int(input("Enter the year:"))
if year % 400 ==0:
    print("Leap Year!")
elif year % 100 ==0:
    print(" Not Leap Year!")
elif year % 4 ==0:
    print("Leap Year!")
else:
    print("Not Leap Year!")