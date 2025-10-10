def metre_to_feet(m):
    return(m)
def kilometre_to_mile(k):
    return(k)
print("-----------------------")
print("Length Converter:")
print("1.metre_to_feet")
print("2.kilometre_to_mile")
print("-----------------------")
choice = int(input("Enter your own choice:"))
length = float(input("Enter your length value:"))
if choice == 1:
    result = metre_to_feet(length)
    print(f"Result: {result:0.2f}")
elif choice == 2:
    result = kilometre_to_mile(length)
    print(f"Result: {result:0.2f}")
else:
    print("INVALID CHOICE!.Please try again!")