v = int(input('Informe a velocidade do carro: '))

if v > 80:
    print('Você está {}km acima do limite de velocidade. Será multado em R${:.2f}'.format(v-80, (v-80)*7))
