s = 0

for c in range(2, 51, 2):
    if c % 2 == 0:
        print(c, end=' ')
        s += 1
print('\nO total de números pares é igual a {}'.format(s))
