m = int(input("Enter the amount:"))

note = m // 100
print("100 taka note is",note)
m = m % 100

note = m // 50
print("50 taka note is",note)
m = m % 50

note = m // 20
print("20 taka note is",note)
m = m % 20

note = m // 10
print("10 taka note is",note)
m = m % 10

note = m // 5
print("5 taka note is",note)
m = m % 5

note = m // 2
print("2 taka note is",note)
m = m % 2

print("1 taka note is",m)