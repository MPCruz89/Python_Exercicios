lista = []

while True:
    n = int(input('Digite um valor: '))
    if n in lista:
        print('Valor duplicado! Não vou adicionar...')
    else:
        lista.append(n)
        print('Valor adicionado com sucesso...')
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()
    while resp not in 'SN':
        resp = str(input('Valor inválido! Digite [S/N]')).upper().strip()
    if resp in 'Nn':
        break
print(f'Você digitou {len(lista)} números')
lista.sort()
print(lista)