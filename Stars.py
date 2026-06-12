import turtle

# Setup screen and turtle
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Star Pattern - Maisara's First Project")

t = turtle.Turtle()
t.speed(5)
t.color("yellow")
t.pensize(3)

# Draw star
for i in range(5):
    t.forward(200)
    t.right(144)

turtle.done()
