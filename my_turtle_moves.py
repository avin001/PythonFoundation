import turtle

turtle = turtle.Turtle()

def make_moves(distance):
    turtle.forward(distance)
    turtle.left(distance)


x = 1
while x < 190:
    make_moves(x)
    x = x + 1
