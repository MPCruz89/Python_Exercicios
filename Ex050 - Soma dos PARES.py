s = 0
cont = 0

for c in range(1, 7):
    n = int(input('Informe o {}º número: '.format(c)))
    if n % 2 == 0:
        s += n
        cont += 1
print('Você informou {} números pares e a soma deles é {}'.format(cont, s))