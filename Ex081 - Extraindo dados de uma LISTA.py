lista = []

while True:
    lista.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resp == 'N':
        break
print('-=' * 25)
print(f'Você digitou {len(lista)} números')
print(f'Os valores em ordem decrescente são {sorted(lista, reverse=True)}')

lista2 = sorted(lista, reverse=True)
if 5 in lista2:
    for n in range(0, len(lista2)):
        if lista2[n] == 5:
            print(f'O valor 5 está na posição {n}')
else:
    print('O valor 5 não foi encontrado na lista')