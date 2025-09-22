def area_of_square(side):
    area = side **2
    return area
def area_of_rectangle(length,width):
    area =length * width
    return area
def area_of_circle(radius):
    area = 3.14159 * radius **2
    return area
def area_of_triangle(base,height):
    area = 0.5 * base * height
    return area

print("-------------------------------------")
print("------------Area Calculater----------")
print("-------------------------------------")
print("Choose a shape to calculate a area")

print("1.Square")
print("2.Rectangle")
print("3.Circle")
print("4.Triangle")
choice = int(input("Enter your choice:"))

if choice ==1:
    side = float(input("Enter the side lenght of the square:"))
    area= area_of_square(side)
    print(f"The area of the square is,{area:0.2f}")
elif choice ==2:
    lenght = float(input("Enter the lenght of the rectangle:"))
    width = float(input("Enter the width of the rectangle:"))
    area = area_of_rectangle(lenght,width)
    print(f"The area of the circle is: {area:0.2f}")
elif choice == 3:
    radius = float(input("Enter the radius of cricle:"))
    area = area_of_circle(radius)
    print(f"The area of the circle is: {area:0.2f}")
elif choice == 4:
    base = float(input("Enter the base of the rectangle:"))
    height = float(input("Enter the height of the rectangle:"))
    area = are_of_triangle(base,height)
    print(f"The area of the circle is: {area:0.2f}")

else:
    print("Invalid choice.please try again!")