n = int(input('Informe um número inteiro: '))

m = n // 1000
c = (n % 1000) // 100
d = (n % 100) // 10
u = n % 10

print('unidade = {}'.format(u))
print('dezena = {}'.format(d))
print('centena = {}'.format(c))
print('milhar = {}'.format(m))
