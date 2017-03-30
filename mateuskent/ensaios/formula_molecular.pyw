import re
formula = input('Fórmula Molecular: ')

elementos = {
            'H':'Hidrogênio',
            'C':'Carbono',
            'O':'Oxigênio',
            'N':'Nitrogênio',
            'Na':'Sódio',
            'Cl':'Cloro',
            'Fe':'Ferro',            
            'S':'Enxofre',
            'Mg':'Magnésio',
            'Al':'Alumínio',
            'Ca':'Cálcio',
            'Cu':'Cobre',
            'F':'Flúor',
            'K':'Potássio',
            'P':'Fósforo',
            }

dados_da_molecula = {}

atomos = re.findall('[A-Z][a-z]?\d*', formula)

for i in atomos:
    dados_da_molecula[re.findall('[A-Z][a-z]?', i)[0]] = re.findall('\d+', i)[0]\
                                                         if re.findall('\d+', i) != []\
                                                         else 1

for chave in dados_da_molecula.keys():
    if dados_da_molecula[chave] == 1:
        print('Existe {} átomo de {} na fórmula {}.'.format(dados_da_molecula[chave], elementos[chave], formula))
    else:
        print('Existem {} átomos de {} na fórmula {}.'.format(dados_da_molecula[chave], elementos[chave], formula))
