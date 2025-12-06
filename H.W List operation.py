names = ["Amber", "Lamia","Anya","bella","Archena","Nameera","Cathy","Clair","Sara","Sumere"]

print(names)
print(len(names))
print(names[0])
print(names[-1])

names.append("Pervini")
print(names)

names.insert(3,"Leen")
print(names)

names.remove("Cathy")
print(names)
pooped = names.pop()
print(pooped)
print(names)

print("Lamia" in names)

names.sort()
print(names)
marks = [10, 13, 25, 34, 67]
marks.sort()
print(marks)

marks.reverse()
print(marks)
