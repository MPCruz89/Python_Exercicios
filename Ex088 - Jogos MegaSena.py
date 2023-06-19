from time import sleep
from random import randint
jogo = []

print('-'* 30)
print('{:^25}'.format('JOGA NA MEGA SENA'))
print('-'* 30)

n = int(input('Quantos jogos você quer que eu sorteie? '))
print('SORTEANDO {} JOGOS'.format(n))

for n in range(0, n):
    print(f'Jogo {n+1}: ', end='')
    while len(jogo) <= 5:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
    print(sorted(jogo))
    sleep(.7)
    jogo.clear()
print('{:=^30}'.format('BOA SORTE'))

