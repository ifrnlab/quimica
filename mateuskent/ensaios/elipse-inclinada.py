import turtle
from math import sqrt, sin, cos, pi

tela = turtle.Screen()
eletron = turtle.Turtle()
eletron.shape('circle')
eletron2 = turtle.Turtle()
eletron2.shape('circle')

a = 100
a2 = 50
b = a/2
b2 = a2*2 
eletron.up()
eletron.setpos(a,0)
eletron.down()
eletron2.up()
eletron2.setpos(a2,0)
eletron2.down()

'''while True:
    for angulo in range(361):
        r = raio*sin(3*(pi*angulo/180))
        x = r*cos(pi*angulo/180)
        y = r*sin(pi*angulo/180)
        eletron.setpos(x,y)'''
        
while True:
    for angulo in range(361):
        r = (a * b)/sqrt(a**2*sin(pi*angulo/180)**2 + b**2*cos(pi*angulo/180)**2)
        r2 = (a2 * b2)/sqrt(a2**2*sin(pi*angulo/180)**2 + b2**2*cos(pi*angulo/180)**2)
        x = r*cos(pi*angulo/180)
        x2 = r2*cos(pi*angulo/180)
        y = r*sin(pi*angulo/180)
        y2 = r2*sin(pi*angulo/180)
        xr = x*cos(pi/4) - y*sin(pi/4)
        yr = x*sin(pi/4) + y*cos(pi/4)
        eletron.setpos(xr,yr)
        eletron.speed(10)
        eletron2.setpos(x2,y2)
