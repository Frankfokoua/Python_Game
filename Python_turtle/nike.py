"""
import turtle
from random import uniform

t= turtle.Turtle()

turtle.bgcolor("black")
t.goto(-50, 100)
t.ht()
t.begin_fill()
t.fillcolor(uniform(0,1), uniform(0,1), uniform(0,1))
t.pencolor("white")
t.pensize(5)
t.lt(200)
t.circle(50, 200)
t.fd(200)
t.lt(173)
t.fd(180)
t.circle(-40, 150)
t.end_fill()

t.up()
t.goto(-70, -90)
t.down()
for i in range (100):
    t.color(uniform(0,1), uniform(0,1), uniform(0,1))
    t.write("NIKE", font=("Arial", 30, "bold"))

turtle.done()"""