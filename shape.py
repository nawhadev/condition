import turtle
turtle.Screen().bgcolor('red')

turtle.Screen().setup(600,500)

p =turtle.Turtle()
p.color('white')
p.pensize(5)
p.shape('turtle')

n = 8

for i in range(n):
    p.forward(100)
    p.right(360/n)
turtle.done()