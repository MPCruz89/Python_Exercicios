from time import sleep
from random import randint

numeros = []

def sorteia():
    c = n = 0
    while c < 5:
        n = randint(1, 10)
        numeros.append(n)
        c += 1
    print(f'Sorteando 5 valores da lista: ', end=' ')
    for num in numeros:
        print(num, end=' ')
        sleep(.3)
    print('PRONTO!!')


def somaPar():
    soma = 0
    for num in range(0, len(numeros)):
        if numeros[num] % 2 == 0:
            soma += numeros[num]
    print(f'Somando os valores pares de {numeros}, temos {soma}')


sorteia()
somaPar()