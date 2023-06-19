peso = float(input('Informe seu peso: (Kg) '))
alt = float(input('Informe sua altura: (m) '))

imc = (peso/(alt * alt))

if imc < 18.5:
    print('Seu IMC é de {:.2f}. Você está abaixo do Peso'.format(imc))
elif imc < 25:
    print('Seu IMC é de {:.2f}. Você está no Peso Ideal'.format(imc))
elif imc < 30:
    print('Seu IMC é de {:.2f}. Você está de Sobrepeso'.format(imc))
elif imc < 40:
    print('Seu IMC é de {:.2f}. Você está Obeso'.format(imc))
else:
    print('Seu IMC é de {:.2f}. Você está em Obesidade Mórbida'.format(imc))