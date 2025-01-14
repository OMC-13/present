from turtle import *
import colorsys
import math

speed(0.02)
bgcolor("black")

# Genera los petalos
goto(0, -40)
h = 0

for i in range(16):
    for j in range(18):
        c= colorsys.hsv_to_rgb(0.125 , 1, 1)
        color(c)
        rt(90)
        circle(150-j*6, 90)
        lt(90)
        circle(150-j*6, 90)
        rt(180)
    circle(40, 24)

# Genera la parte centrall de la flor
color("black") 
shape("turtle")
fillcolor("brown")
phi = 137.508 * (math.pi/ 180.0)

for i in range (200):
    r = 4 * math.sqrt(i)
    theta = i*phi
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    penup()
    goto(x, y)
    setheading(i * 137.508)
    pendown()
    stamp()

penup()
goto(0, -200)  # Posiciona el texto en la parte inferior de la flor
pendown()
color("white")  # Cambia el color del texto
write("“Te regalo esta flor para que me regales una sonrisa… o algo más.”", align="center", font=("Arial", 16, "normal"))

done()