a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
c = int(input("Enter the third number:"))
if a<b and a<c:
    print("Th esmallest number is",a)
elif b<a and b<c:
    print("The sammlest number is",b)
else:
    print("the smallest number is",c)