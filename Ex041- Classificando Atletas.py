from datetime import date

ano_nasc = int(input('Informe o ano de seu nascimento: '))

idade = date.today().year - ano_nasc

if idade < 9:
    print('Você tem {} anos. Sua categoria é MIRIM'.format(idade))
elif idade < 14:
    print('Você tem {} anos. Sua categoria é INFANTIL'.format(idade))
elif idade < 19:
    print('Você tem {} anos. Sua categoria é JUNIOR'.format(idade))
elif idade < 20:
    print('Você tem {} anos. Sua categoria é SÊNIOR'.format(idade))
else:
    print('Você tem {} anos. Sua categoria é MASTER'.format(idade))