"""import turtle

d= turtle.Turtle()
s= turtle.Screen()
d.speed(0)
d.pensize(2)
d.pencolor("white")
s.bgcolor("black")

def s_curve():
    for i in range(90):
        d.left(1)
        d.forward(1)

def r_curve():
    for i in range(90):
        d.right(1)
        d.forward(1)

def l_curve():
    s_curve()
    d.forward(80)
    s_curve()

def l_curve1():
    s_curve()
    d.forward(90)
    s_curve()

def half():
    d.forward(50)
    s_curve()
    d.forward(90)
    l_curve()
    d.forward(40)
    d.left(90)
    d.forward(80)
    d.right(90)
    d.forward(10)
    d.right(90)
    d.forward(120) #on test
    l_curve1()
    d.forward(30)
    d.left(90)
    d.forward(50)
    r_curve()
    d.forward(40)
    d.end_fill()

def get_pos():
    d.penup()
    d.forward(20)
    d.right(90)
    d.forward(10)
    d.right(90)
    d.pendown()

def eye():
    d.penup()
    d.right(90)
    d.forward(160)
    d.left(90)
    d.forward(70)
    d.pencolor("black")
    d.dot(35)

def sec_dot():
    d.left(90)
    d.penup()
    d.forward(310)
    d.left(90)
    d.forward(120)
    d.pendown()

    d.dot(35)




d.fillcolor("#306998")
d.begin_fill()
half()
d.end_fill()
get_pos()
d.fillcolor("#FFD43B")
d.begin_fill()
half()
d.end_fill()

eye()
sec_dot()

def speed():
    d.speed(2)
    for i in range(100):
        d.lt(90)


turtle.done()


"""