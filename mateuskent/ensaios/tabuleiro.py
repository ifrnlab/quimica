import turtle
pincel = turtle.Pen()
tela = turtle.Screen()
tela.?
dir(tela)
tela.window_height
tela.window_height()
tela.window_width()
tela.setup
tela.setup()
tela.window_width()
tela.window_width()
tela.window_height()
tela.setup?
tela.setup(800,800)
for k in range(8+1):
    x = -400 + k*100
    y = 400 - k*100
    pass
for k in range(8+1):
    x = -400 + k*100
    y = 400 - k*100
    print('x:', x)
    print('y:', y)
def desenha(x1, y1, x2, y2):
    pincel.up()
    pincel.setpos(x1, y1)
    pincel.down()
    pincel.setpos(x2, y2)
for k in range(8+1):
    x = -400 + k*100
    y = 400 - k*100
    desenha(-400, y, 400, y)
    desenha(x, 400, x, -400)
tela.onclick(pincel.goto)
def exibir_posicao(x, y):
    print('({}, {})'.format(x, y))
tela.onclick(exibir_posicao)
-354+400
46//100
(46//100)+1
((-354+400)//100)+1
400-357
((400-357)//100)+1
((-245+400)//100)+1
((-142+400)//100)+1
((400-(-249))//100)+1
def exibir_posicao(x, y):
    print('({}, {})'.format(x, y))
    j = ((x+400)//100)+1
    i = ((400-y)//100)+1
    print('a{}{}'.format(i,j))
tela.onclick(exibir_posicao)
def exibir_posicao(x, y):
    print('({}, {})'.format(x, y))
    j = ((x+400)//100)+1
    i = ((400-y)//100)+1
    print('a{:0}{:0}'.format(i,j))
tela.onclick(exibir_posicao)
def exibir_posicao(x, y):
    print('({}, {})'.format(x, y))
    j = ((x+400)//100)+1
    i = ((400-y)//100)+1
    print('a{:0.0}{:0.0}'.format(i,j))
tela.onclick(exibir_posicao)
def exibir_posicao(x, y):
    print('({}, {})'.format(x, y))
    j = ((x+400)//100)+1
    i = ((400-y)//100)+1
    print('a[{},{}]'.format(i,j))
tela.onclick(exibir_posicao)
