sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    print('Informação Inválida!!')
    sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()
print('Seu sexo é {}'.format(sexo))

