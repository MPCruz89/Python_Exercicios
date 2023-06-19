from datetime import datetime

c_maior = 0
c_menor = 0

for c in range(1, 8):
    ano = int(input('Informe o ano de nascimento da {}ª pessoa: '.format(c)))
    if datetime.today().year - ano >= 18:
        c_maior += 1
    else:
        c_menor += 1

print('Das sete pessoas, {} são maiores e {} são menores de idade!!'.format(c_maior, c_menor))