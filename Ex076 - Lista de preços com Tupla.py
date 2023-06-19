print('-' * 50)
print('{:^50}'.format('LISTAGEM DE PREÇOS'))
print('-' * 50)

listagem = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Mochila', 123.90, 'Livro', 34.90, 'Transferidor', 4.75)

for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print('{:.<40}'.format(listagem[pos]), end='')
    else:
        print('R$', end='')
        print('{:>8.2f}'.format(listagem[pos]))
print('-' * 50)