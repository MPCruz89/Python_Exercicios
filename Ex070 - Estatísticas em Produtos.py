print('-' * 40)
print('{:^40}'.format('SUPERMERCADO ESTRELA'))
print('-' * 40)
total = 0
cont = 0
p_barato = 0
n_barato = ''
c = 0

while True:
    nome = str(input('Nome do Produto: '))
    valor = float(input('Preço: R$'))
    total += valor
    if valor > 1000:
        cont += 1
    if c == 0:
        n_barato = nome
        p_barato = valor
    else:
        if valor < p_barato:
            p_barato = valor
            n_barato = nome
    c += 1
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    print('-' * 40)
    if escolha == 'N':
        break

print(f'Total de compras foi de R${total:.2f}')
print(f'Temos {cont} produtos custando mais de R$1000,00')
print(f'O produto mais barato foi {n_barato} que custou R${p_barato:.2f}')
