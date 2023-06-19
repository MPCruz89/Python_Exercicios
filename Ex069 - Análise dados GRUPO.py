c_idade = c_homem = c_mulher = 0


while True:
    print('-' * 30)
    print('{:^30}'.format('CADASTRE UMA PESSOA'))
    print('-' * 30)
    idade = int(input('Idade: '))
    if idade > 18:
        c_idade += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()
    if sexo == 'M':
        c_homem += 1
    if sexo == 'F' and idade < 20:
        c_mulher += 1
    print('-' * 30)
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if escolha == 'N':
        break
print('{:=^25}'.format('FIM DO PROGRAMA'))
print(f'Total de pessoas com mais de 18 anos: {c_idade}')
print(f'Ao todo temos {c_homem} homens cadastrados.')
print(f'E temos {c_mulher} mulheres com menos de 20 anos.')

