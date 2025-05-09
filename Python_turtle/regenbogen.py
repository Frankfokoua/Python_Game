"""from random import uniform
import turtle
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(0)
c = 0
while True:
    t.pencolor(uniform(0,1),uniform(0,1),uniform(0,1) )
    for i in range(4):
        t.fd(150)
        t.right(90)
    t.right(5)
    c += 1
    if c>= 360/5:
        break
        t.hideturtle()
turtle.done()"""