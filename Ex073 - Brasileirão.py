times = ('Botafogo', 'Palmeiras', 'Cruzeiro', 'Fortaleza', 'São Paulo', 'Fluminense', 'Grêmio', 'Internacional',
'Bahia', 'Atl. Paranaense', 'Vasco da Gama', 'RB Bragantino', 'Cuiabá', 'Santos', 'Atl. Mineiro', 'Flamengo',
'Corinthians', 'Goiás', 'Coritiba', 'Amé. Mineiro')

print('-=' * 15)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 15)
print(f'Os 5 primeiros colocados são: {times[0:5]}')
print('-=' * 15)
print(f'Os 4 últimos colocados são: {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
for pos, clube in enumerate(times):
    if clube == 'Fortaleza':
        print(f'O {clube} está na {pos + 1}ª posição')
print('-=' * 15)