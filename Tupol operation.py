marks = (10, 20, 30, 40, 50)
fruits = ("apple", "banana", "cherry", "banana")

print("1.Accessing on Element:", marks[2])
print("2.Slicing:", marks[1:4])
print("3.Length:", len(fruits))
print("4.Count:", fruits.count("banana"))
print("5.Index:", fruits.index("cherry"))

t3 = marks + fruits
print("6. Concatation:", t3)
t4 = marks * 2
print("7.Repitation:", t4)
print("8. Membership Check:", 30 in marks)
lst = list(marks)
print("Tuple to list:",lst)
