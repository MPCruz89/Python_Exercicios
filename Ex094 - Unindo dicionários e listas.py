pessoa = {}
geral = []
soma_idade = 0

while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['idade'] = int(input('Idade: '))
    soma_idade += pessoa['idade']
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F]')).upper().strip()
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor digite somente M ou F.')
    geral.append(pessoa.copy())
    while True:
        resp = str(input('Deseja continuar? [S/N]')).strip().upper()
        if resp in 'SN':
            break
        print('ERRO! Digite S ou N.')
    if resp == 'N':
        break
media_idade = soma_idade / len(geral)
print(geral)
print('-=' * 30)
print(f' A) O grupo tem {len(geral)} pessoas cadastradas.')
print(f' B) A média de idade é de {media_idade:.2f} anos.')
print(f' C) As mulheres cadastradas foram ', end='')
for p in geral:
    if p['sexo'] == 'F':
        print(p['nome'], end=' ')
print('\n D) Lista das pessoas que estão acima da média:')
for p in geral:
    if p['idade'] > media_idade:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')
