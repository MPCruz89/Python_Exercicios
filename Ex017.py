from math import hypot

co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))

print('Você digitou o cateto oposto {} e o cateto adjacente {}. A hipotenusa tem valor {:.2f}.'.format(co, ca, hypot(co, ca)))



