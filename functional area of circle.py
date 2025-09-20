def  areaOfCircle(r):
    area = 3.14159 * r * r
    area =round(area,2)
    return area
radius = float(input("Enter the radius of circle:"))
print("The area of circle is",areaOfCircle(radius))