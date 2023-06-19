lista = [[], [], []]
soma_pares = 0
soma_tres_coluna = 0
maior_linha_dois = 0

for l in range(0, 3):
    for c in range(0, 3):
        num = int(input(f'Digite um valor para [{l}, {c}]: '))
        if num % 2 == 0:
            soma_pares += num
        if c == 2:
            soma_tres_coluna += num
        lista[l].append(num)
        if l == 1:
            for c in range(0, 3):
                if c == 0:
                    maior_linha_dois = num
                else:
                    if num > maior_linha_dois:
                        maior_linha_dois = num
print('-=' * 25)

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[  {lista[l][c]}  ]', end='')
    print(end='\n')
print('-=' * 25)

print(f'A soma dos valores pares é {soma_pares}')
print(f'A soma dos valores da terceira coluna é {soma_tres_coluna}')
print(f'O maior valor da segunda linha é {maior_linha_dois}')