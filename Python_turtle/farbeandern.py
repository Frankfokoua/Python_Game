"""from turtle import*
from time import sleep
from random import uniform

bgcolor("black")
t = [Turtle(), Turtle()]
x = 3

colors = ['red','yellow', 'blue','lime']

for index, i in enumerate(t):
    i.speed(0)
    i.color('green')
    i.shapesize(0.3)
    i.width(3)
    i.pu()
    i.seth(90)
    i.fd(150)
    i.seth(-180)
    i.pd()
t[0].pu()
speed(0)
delay(0)
ht()
sleep(4)

for i in colors:
    color(uniform(0,1), uniform(0,1), uniform(0,1))
    for i in range(360):
        t[0].fd(x)
        t[0].lt(1)
        pu()
        goto(t[0].pos())
        pd()
        t[1].fd(2*x)
        t[1].lt(2)
        goto(t[1].pos())
done()"""