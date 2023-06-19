# n = int(input('Digite um número para verificar se ele é primo: '))
# lista = []
#
# for c in range(2, n-1):
#     if n % c == 0:
#         lista.append(c)
# if len(lista) == 0:
#     print('{} é um número primo!!'.format(n))
# else:
#     print('{} NÃO é primo!!'.format(n))

n = int(input('Digite um número: '))
tot = 0
for c in range(1, n+1, 1):
    if n %c == 0:
        print('\033[34m', end= '')
        tot += 1
    else:
        print('\033[31m', end= '')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes'.format(n, tot))

if tot == 2:
    print('Portanto, o número {} \033[34mÉ PRIMO\033[m'.format(n))
else:
    print('Portante, o número {} \033[31mNÃO É PRIMO\033[m'.format(n))