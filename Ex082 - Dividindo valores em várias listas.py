lista = []
lista_par = []
lista_impar = []

while True:
    lista.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N] ')).strip()
    if resp in 'Nn':
        break
for n in range(0, len(lista)):
    if lista[n] % 2 == 0:
        lista_par.append(lista[n])
    else:
        lista_impar.append(lista[n])

print('-=' * 25)
print(f'A lista completa ordenada é {sorted(lista)}')
print(f'A lista de pares ordenada é {sorted(lista_par)}')
print(f'A lista de ímpares ordenada é {sorted(lista_impar)}')
