from random import randint
from time import sleep
from operator import itemgetter

resultados = {'jogador1': randint(1, 6),
              'jogador2': randint(1, 6),
              'jogador3': randint(1, 6),
              'jogador4': randint(1, 6)
              }

ranking = {}
for k, v in resultados.items():
    print(f'O {k} tirou {v}.')
    sleep(.5)

print('RANKING DOS JOGADORES')
'''for i in sorted(resultados, key=resultados.get, reverse=True):
    print(f'    º lugar: {i} com {resultados[i]}')'''

ranking = sorted(resultados.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} tirou {v[1]}')
