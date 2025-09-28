def area_of_square(side):
    area = side **2
    return area
def area_of_rectangle(lenth,width):
    area = length * width
    return area
def area_of_circle(radius):
    area = 3.14159 *radius * r
    return area
def area_of_triangle(base,height):
        area= 0.5 * base * height
        return area
print("-------------Area Calculater------------")
print("-----------------------------------------")
print("Choose a shape to calculate the area")

print("1.square")
print("2.rectangle")
print("3.circle")
print("4.triangle")
choice = int(input("Enter you choice:"))
if choice == 1:
    side = float(input("Enter the side of the square:"))
    area = area_of_square(side)
    print(f"Your area of the square is {area:0.2f}")
elif choice == 2:
    length = float(input("Enter the length of the square:"))
    width = float(input("Enter the width of the rectangle:"))
    area = area_of_rectangle(length,width)
    print(f"Your area of the rectangle is {area:0.2f}")
elif choice == 3:
    radius = float(input("Enter the radius of the circle:"))
    area = area_of_circle(radius)
    print(f"Your area of the circle is {area:0.2f}")
elif choice == 4:
    base = float(input("Enter the base of the triangle:"))
    height = float(input("Enter the height of the triangle:"))
    area = area_of_triangle(base,height)
    print(f"The area of the triangle is {area :0.2f}")
else:
    print("Invalid choice!")
