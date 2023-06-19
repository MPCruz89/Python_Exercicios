lista = []

for cont in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {cont+1}: ')))
    if cont == 0:
        maior = lista[cont]
        menor = lista[cont]
    else:
        if lista[cont] > maior:
            maior = lista[cont]
            pos_maior = cont+1
        if lista[cont] < menor:
            menor = lista[cont]
            pos_menor = cont+1

print('-=' * 25)
print(f'Você digitou os valores {lista}')
print(f'Maior número é {maior} nas posições ', end='')
for c, v in enumerate(lista):
    if v == maior:
        print(f'{c+1}...', end='')
print(f'\nMenor número é {menor} nas posições ', end='')
for c, v in enumerate(lista):
    if v == menor:
        print(f'{c+1}...', end='')
