import turtle
from turtle import Turtle
from math import sqrt, sin, cos, pi

class Astro(Turtle):
    def __init__(self, nome, tamanho, cor):
        Turtle.__init__(self)
        self.nome = nome
        self.tamanho = tamanho
        self.cor = cor
        self.shapesize(tamanho, tamanho)

class Estrela(Astro):
    def __init__(self, nome, tamanho, cor):
        Astro.__init__(self, nome, tamanho, cor)
        self.shape('circle')
        self.color(cor)
        self.shapesize(tamanho, tamanho)
        
class Planeta(Astro):
    def __init__(self, nome, tamanho, cor, posicao_orbita):
        Astro.__init__(self, nome, tamanho, cor)
        self.posicao_orbita = posicao_orbita
        
#       Esta parte comentada ainda não funciona adequadamente, pois não sei mudar o
#       tamanho do objeto quando sua forma é uma imagem.GIF.

        '''
        tela.register_shape(nome+'.gif')
        self.shape(nome+'.gif')
        self.resizemode("user")
        '''
        
        self.shape('circle')
        self.color(cor)
        self.shapesize(tamanho, tamanho,0)
        self.pencolor('blue')
        self.speed('fastest')
        self.hideturtle()

    def translacao(self, angulo):
        # Se for o planeta Plutão, sua órbita tem que ser uma elipse inclinada em relação ao Sol.
        if self.posicao_orbita == 9:
            a = self.posicao_orbita * raio
            b = a/2        
            r = (a * b)/sqrt(a**2*sin(pi*angulo/180)**2 + b**2*cos(pi*angulo/180)**2)            
            x = r*cos(pi*angulo/180)
            y = r*sin(pi*angulo/180)
            x = x*cos(pi/4) - y*sin(pi/4)
            y = x*sin(pi/4) + y*cos(pi/4)
            if angulo == 0:
                self.up()
                self.setpos(x,y)
                self.down()
                self.showturtle()  
            self.setpos(x,y)

        # Os outros planetas não têm uma órbita inclinada em relação ao Sol.
        else:
            a = self.posicao_orbita * raio
            b = a/2        
            r = (a * b)/sqrt(a**2*sin(pi*angulo/180)**2 + b**2*cos(pi*angulo/180)**2)            
            x = r*cos(pi*angulo/180)
            y = r*sin(pi*angulo/180)
            if angulo == 0:
                self.up()
                self.setpos(x,y)
                self.down()
                self.showturtle()  
            self.setpos(x,y)


tela = turtle.Screen()
raio = 60
tela.bgcolor('black')

sol = Estrela('Sol',2,'gold')

mercurio = Planeta('Mercúrio', 0.3, 'gray', 1)
venus = Planeta('Vênus', 0.5, 'darkorange', 2)
terra = Planeta('Terra', 0.6, 'blue', 3)
marte = Planeta('Marte', 0.4, 'red', 4)
jupiter = Planeta('Júpiter', 1.0, 'sandybrown', 5)
saturno = Planeta('Saturno', 0.9, 'goldenrod', 6)
urano = Planeta('Urano', 0.8, 'mediumseagreen', 7)
netuno = Planeta('Netuno', 0.7, 'steelblue', 8)
plutao = Planeta('Plutão', 0.1, 'peachpuff', 9)

while True:
    for i in range(361):    
        mercurio.translacao(i*10)
        venus.translacao(i*9)
        terra.translacao(i*8)
        marte.translacao(i*5)
        jupiter.translacao(i*4)
        saturno.translacao(i*3)
        urano.translacao(i*2)
        netuno.translacao(i*1)
        plutao.translacao(i)
