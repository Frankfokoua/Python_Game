"""import turtle
from random import uniform
t = turtle.Turtle()
turtle.bgcolor("black")
speed = 0 # Geschwindigkeit des Fraktals
angle = 20 # Winkel des Fraktals
length = 100 # Länge des Fraktals

def fractal(size):
    if size < 10:
        t.pencolor(uniform(0,1), uniform(0,1), uniform(0,1))
        return
    else:
        
        t.pencolor(uniform(0,1), uniform(0,1), uniform(0,1))
        t.forward(size)
        t.left(angle)
        fractal(size/2)
        t.right(angle*2)
        fractal(size/2)
        t.left(angle)
        t.backward(size)

while True:
    t.pencolor(uniform(0,1), uniform(0,1), uniform(0,1))
    fractal(length)
    t.right(10)

turtle.done()"""