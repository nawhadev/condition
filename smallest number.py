a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
c = int(input("Enter the third number:"))
if a<b and a<c:
    print("The smallest number is",a)
elif b<a and b<c:
    print("The smallest number is",b)
else:
    print("The greatest number is",c)