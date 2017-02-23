''' Movimento Retilíneo Acelerado'''

import turtle
janela = turtle.Screen()
janela.screensize(400,300)
c = turtle.Turtle()
c.shape('turtle')
#c.speed('fastest')
c.up()
a = -4
while True:
    c.setpos(0,400)
    # Queda com a=-4
    for t in range(20):
        y = 400+(a/2)*t**2
        c.setpos(0,y)
        
    # Subida com v0=-4*20 = -80
    x0, y0 = c.position()
    for t in range(20):
        y = y0 + 75*t +(a/2)*t**2
        c.setpos(0,y)
