import turtle
import random

turtle.Screen().bgcolor('black')
turtle.Screen().setup(500, 500)
turtle.Screen().title('Circle Pattern')
t= turtle.Turtle()
t.pensize(2)
size = 0
color= ['red','yellow', 'blue','orange']

while True:
    r = 10 #radius
    t.color(random.choice(color))
    for i in range(100):
        t.circle(r + i, 45)
