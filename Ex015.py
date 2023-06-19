dias = int(input('Quantos dias você alugou o carro? '))
km = int(input('Quantos km você percorreu? '))

total = (60 * dias) + (0.15 * km)

print('Você alugou o carro por {} dias e percorreu {}kms. Preço final igual a R${:.2f}.'.format(dias, km, total))
