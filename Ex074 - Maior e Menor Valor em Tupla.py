from random import  randint
tupla = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10),)

maior = 0
menor = 0
print('Os valores sorteados foram ', end='')
for n in range(0, len(tupla)):
    print(tupla[n], end=' ')
    if n == 0:
        maior = tupla[0]
        menor = tupla[0]
    else:
        if tupla[n] > maior:
            maior = tupla[n]
        if tupla[n] < menor:
            menor = tupla[n]

print(f'\nO maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')
print(max(tupla))
print(min(tupla))