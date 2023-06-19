s = 0
soma = 0

for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
        soma = soma + 1
print('A soma dos {} números solicitados é \033[1;33m{}\033[m,'.format(soma, s))