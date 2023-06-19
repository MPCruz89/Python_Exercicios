dados = {}
gols = []
totgols = 0
dados['nome'] = str(input('Nome do jogador: '))
totpartidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))

for g in range(0, totpartidas):
    gols.append(int(input(f'Quantos gols na partida {g+1}? ')))
    dados['gols'] = gols

for g in gols:
    totgols += g
dados['total'] = totgols
print('-='*30)
print(dados)
print('-='*30)

for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {dados["nome"]} jogou {totpartidas} partidas.')
for i in range(0, totpartidas):
    print(f'   => Na partida {i+1}, fez {dados["gols"][i]} gols.')
print(f'Foi um total de {totgols}')
