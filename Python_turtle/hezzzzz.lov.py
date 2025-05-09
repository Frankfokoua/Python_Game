"""import turtle
import math
from random import uniform

t= turtle.Turtle()
s= turtle.Screen()
turtle.bgcolor("black")
t._color("black")
t.speed(0)
t.ht()
s.tracer(0,0)

def draw_heart(alpha,d):
    r = d/math.tan(math.radians(180-alpha/2))
    t.up()
    t.goto(0,-d*math.cos(math.radians(45)))
    t.seth(90-(alpha-180))
    t.down()
    t.begin_fill()
    t.fd(d)
    t.circle(r,alpha)
    t.left(180)
    t.circle(r,alpha)
    t.fd(d)
    t.end_fill()

def  figure6 ():    
    t.pencolor(uniform(0,1),uniform(0,1),uniform(0,1) )
    t.penup()
    t.goto(-140, -200)
    t.pendown()
    t.write("I LOVE YOU BABY :)" , font=("Arial", 20, "bold"))
a = 220
sign = -1

def animate():
  t.color("red")
  global a,sign
  t.clear()
  draw_heart(a,200)
  a += sign
  figure6()
  if a < 215:    
    sign = -sign
  elif a > 220:   
    sign = -sign
  s.ontimer(animate,50)
  
animate()
turtle.done()"""