import turtle
from turtle import *

pen = turtle.Turtle()
pen.speed(2)
pen.hideturtle()
x = 180

def right():
    pen.left(45)
    pen.forward(x)
    pen.right(135)
    pen.forward(x)
    pen.right(45)
    pen.forward(x)
    pen.right(135)
    pen.forward(x)

def left():
    pen.left(45)
    pen.forward(x)
    pen.left(135)
    pen.forward(x)
    pen.left(45)
    pen.forward(x)
    pen.left(135)
    pen.forward(x)

def top():
    pen.left(45)
    pen.forward(x)
    pen.right(90)
    pen.forward(x)
    pen.right(90)
    pen.forward(x)
    pen.right(90)
    pen.forward(x)
    pen.right(135)
    pen.forward(x)

pen.color("red")

pen.begin_fill()
right()

pen.end_fill()

pen.color("blue")

pen.begin_fill()
left()

pen.end_fill()

pen.color("yellow")

pen.begin_fill()
top()

pen.end_fill()


done()
