import turtle

turtle = turtle.Turtle()
turtle.speed(20)


def make_moves(distance):
    turtle.forward(distance)
    turtle.left(distance)


x = 1
while x < 190:
    make_moves(x)
    x = x + 1
