from datetime import date

dados = {}

dados['nome'] = str(input('Nome: '))
ano_nasc = int((input('Ano de nascimento: ')))
dados['idade'] = date.today().year - ano_nasc
dados['ctps'] = int(input('Carteira de Trabalho: (0 se não tem) '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = (dados['contratação'] + 35) - ano_nasc

print('-=' * 25)
for k, v in dados.items():
    print(f'{k} tem o valor {v}')
