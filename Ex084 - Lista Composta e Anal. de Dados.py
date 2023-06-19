pessoas = []
dados = []
cont = 0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if resp == 'N':
        break

for c in range(0, len(pessoas)):
    if c == 0:
        maior = pessoas[c][1]
        menor = pessoas[c][1]
    else:
        if pessoas[c][1] > maior:
            maior = pessoas[c][1]
        if pessoas[c][1] < menor:
            menor = pessoas[c][1]
    cont +=1

print('-=' * 25)
print(f'Ao todo, você cadastrou {cont} pessoas')
print(f'O maior peso foi de {maior}kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'{p[0]}...', end=' ')

print(f'\nO menor peso foi de {menor}kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'{p[0]}...', end=' ')