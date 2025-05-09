"""import turtle as turtle

turtle.pensize(8)
turtle.speed(20)

def drawCircle(circleColor, posX, posY, fullCircle=False):
    turtle.color(circleColor)
    turtle.penup()
    turtle.goto(posX, posY)
    turtle.pendown()
    for _ in range(0 if fullCircle else 2):
        turtle.circle(45, 82)
        turtle.penup()
        turtle.circle(45, 18)
        turtle.pendown()
    turtle.circle(45, 360 if fullCircle else 160)

drawCircle('blue', -2*45 - 2*8, 0, True)
drawCircle('black', 0, 0, True)
drawCircle('red', 2*45 + 2*8, 0, True)
drawCircle('yellow', -45 - 8, -45)
drawCircle('green', 45 + 8, -45)

turtle.done()"""