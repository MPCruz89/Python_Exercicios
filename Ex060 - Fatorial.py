n = int(input('Digite um número para calcular seu fatorial: '))

fat = 1
cont = 1
c = n

print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    fat = fat * cont
    cont += 1
    c -= 1
print('{}'.format(fat))

