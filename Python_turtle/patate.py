"""
from random import uniform
import turtle
import math

t = turtle.Turtle()
turtle.bgcolor("black")
t.speed(10000)
t.pensize(3)
t.up()
t.goto(50,-100)
t.down()
t.shape("turtle")

t.begin_fill()

for i in range(2000):
    t.color(uniform(0,1),uniform(0,1), uniform(0,1))
    t.forward(10)
    t.left(math.sin(i/10)*25)
    t.left(20)

turtle.mainloop()"""