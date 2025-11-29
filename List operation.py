names =["Arif", "Nishat", "Sumaiya", "Rafi",  "Tania", "Jaber", "Lania", "Mamun", "Sadia", "Imran",]

print(names)
print(len(names))
print(names[0])
print(names[-1])

names.append("Sofia")
print(names)

names.insert(2,"Khaidja")
print(names)

names.remove("Rafi")
print(names)
pooped = names.pop()
print(pooped)
print(names)

print("Lamia" in names)

names.sort()
print(names)

marks = [25, 12, 39, 28, 59, 35]
marks.sort()
print(marks)

marks.reverse()
print(marks)