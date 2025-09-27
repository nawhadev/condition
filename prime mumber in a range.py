b = int(input("Enter the starting range:"))
n = int(input("Enter the last range:"))
print("****************")
print("Prime numbers-")
print("****************")
for i in range(b,n+1):
    if i > 1:
        for j in range (2,i):

            if i%j ==0:
                break
            else:
                print(i, end=" ")