def celsius_to_farenheight(c):
    return  c * 9/5 * 32
def farenheight_to_celsius(f):
    return  f * -32 * 5/9
print("Temperature Converter")
print("1.celsius to farenheight")
print("2.farenheight to celsius")
choice = int(input("Enter your choice(1 or 2):"))
temperature = float(input("Enter the temperature value:"))
if choice == 1:
    result = celsius_to_farenheight(temperature)
    print(f"Result: {result:0.2f}")
elif choice == 2:
    result = farenheight_to_celsius(temperature)
    print(f"Result: {result:0.2f}")
else:
    print("Invalid choice.Please try again")