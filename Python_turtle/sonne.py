"""from turtle import speed, bgcolor, colormode, fd, rt, pencolor, done, circle, goto


speed(0)
bgcolor('black')
r, g, b = 255, 0, 0
goto(0, -200)
for i in range(170):
    colormode(255)
    
    if i < 255//3:
        g += 3
    elif i < (255*2)//3:
        r -= 3
    elif i < 255:
        b += 3
    elif i < (255*4)//3:
        g -= 3
    elif i < (255*5)//3:
        r += 3
    else:
        b -= 3
        
    circle(30+i)
    circle(90)
    pencolor(r, g, b)
done()"""