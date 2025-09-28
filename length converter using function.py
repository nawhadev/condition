def metre_to_feet(m):
    return m * 3.28084
def feet_to_metre(f):
    return f * 0.3048
def kilometer_to_mile(k):
    return k * 0.621371
def mile_to_kilometer(m):
    return m * 1.60934

print("Length Converter")
print("1.Metre to feet")
print("2.Feet to metre")
print("3.Kilometer to mile")
print("4.mile to kilometer")
choice = int(input("Enter your choice(1 or 2):"))
length = float(input("Enter your length value:"))

if choice == 1:
    result = metre_to_feet(length)
    print(f"Result: {result:0.2f}")
elif choice ==2:
    result = feet_to_metre(length)
    print(f"Result: {result:0.2f}")
elif choice ==3:
    result = kilometer_to_mile(length)
    print(f"Result: {result:0.2f}")
elif choice ==4:
    result = mile_to_kilometer(length)
    print(f"Result: {result:0.2f}")
else:
    pritn("Invalis choice!.Please try again!")