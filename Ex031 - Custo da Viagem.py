dist = int(input('Informe a distância da viagem em km: '))

if dist > 200:
    valor = dist * 0.45
else:
    valor = dist * 0.50

print('você vai viajar {} quilômetros e vai pagar R${:.2f}.'.format(dist, valor))


