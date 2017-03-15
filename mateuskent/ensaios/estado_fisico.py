from turtle import Screen, Pen

class Particula:
    
    def __init__(self):
        self._desenho = Pen()
        self._desenho.shape('circle')
        self._desenho.color('blue')
        self._velocidade = (0,0)


    def alterar_velocidade(self, valor):
        pass

class Recipiente:
    pass

class Substancia:

    def __init__(self, materia: str, ponto_fusao: int, ponto_ebulicao: int, temperatura_inicial:int=0):
        self._temperatura = temperatura_inicial
        self._ponto_fusao = ponto_fusao
        self._ponto_ebulicao = ponto_ebulicao
        self._analisar_estado()
        self._particulas = []

    def _analisar_estado(self):
        self._estado = 'sólido' if self._temperatura < self._ponto_fusao else \
                       'líquido' if self._temperatura < self._ponto_ebulicao else \
                       'gasoso'

    def aumentar_temperatura(self):
        self._temperatura += 1
        self._analisar_estado()
        print('Temperatura: {}; Estado: {}'.format(self._temperatura, self._estado))

    def reduzir_temperatura(self):
        self._temperatura -= 1
        self._analisar_estado()
        print('Temperatura: {}; Estado: {}'.format(self._temperatura, self._estado))

    @property
    def temperatura(self):
        return self._temperatura

    @property
    def estado(self):
        return self._estado    
    

def main():
    substancia = Substancia('água', 0, 100, 25)
    tela = Screen()
    tela.listen()
    tela.onkey(substancia.reduzir_temperatura, 'Left')
    tela.onkey(substancia.reduzir_temperatura, 'Down')
    tela.onkey(substancia.reduzir_temperatura, '-')
    tela.onkey(substancia.aumentar_temperatura, 'Right')
    tela.onkey(substancia.aumentar_temperatura, 'Up')
    tela.onkey(substancia.aumentar_temperatura, '+')    
    tela.exitonclick()

if __name__ == '__main__':
    main()

        
