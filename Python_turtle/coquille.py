"""from random import uniform
from turtle import*
bgcolor("black")
speed(0)
hideturtle()
for i in range(130):
    color(uniform(0,1),uniform(0,1),uniform(0,1))
    circle(i)
    color(uniform(0,1),uniform(0,1),uniform(0,1))
    circle(i*0.8)
    right(3)
    forward(3)
done()


'carre'
import turtle
from random import uniform
t= turtle.Turtle()
t.speed(0)
t.ht()
turtle.bgcolor("black")
def draw_square(x,y,size,tilt_angle,c):
    t.up()
    t.goto(x,y)
    t.down()
    t.seth(tilt_angle)
    t.fillcolor(c)
    t.begin_fill()
    for i in range(4):
        t.fd(100)
        t.left(90)
    t.end_fill()
angle=0
size=300
while size > 0:
    draw_square(0,0,size,angle,(uniform(0,1),uniform(0,1),uniform(0,1)))
    size -= 0.1
    angle+=3
turtle.done()"""