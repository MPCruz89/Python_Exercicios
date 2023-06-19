aluno = {}

aluno['Nome'] = str(input('Nome: '))
aluno['Media'] = float(input('Média: '))
if aluno['Media'] >= 7.0:
    aluno['Situacao'] = 'Aprovado'
else:
    aluno['Situacao'] = 'Reprovado'

for k, v in aluno.items():
    print(f'{k} é igual a {v}')