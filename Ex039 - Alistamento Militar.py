from datetime import date

ano_nasc = int(input('Informe o ano de seu nascimento: '))

hoje = date.today().year
idade = hoje - ano_nasc

if idade > 18:
    print('Você tem {} anos e ja passou {} do tempo de se alistar.'.format(idade, idade - 18))
elif idade < 18:
    print('Você tem {} anos e ainda faltam {} anos para você se alistar'.format(idade, 18 - idade))
else:
    print('Você tem {} anos e precisa se alistar'.format(idade))
