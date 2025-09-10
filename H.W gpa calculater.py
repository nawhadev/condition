grade =int(input("Enter the marks:"))

if 80 <= grade <= 100:
    print("A+")
elif 70 <= grade <= 79:
    print("A")
elif 60 <= grade <= 69:
    print("A-")
elif 50 <= grade <= 59:
    print("B")
elif 40 <= grade <= 49:
    print("C")
elif 33 <= grade <= 39:
    print("D")
else:
    print("F")