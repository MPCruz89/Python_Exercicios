lista = [[], []]

for n in range(0, 7):
    num = int(input(f'Digite o {n+1}º valor: '))
    if num % 2 == 0:
        lista[0].append(num)
    else:
       lista[1].append(num)
print('-=' * 30)
print(f'Os valores pares digitados foram {sorted(lista[0])}')
print(f'Os valores ímpares digitados foram {sorted(lista[1])}')