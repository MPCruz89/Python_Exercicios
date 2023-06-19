f = input('Digite uma frase qualquer: ').strip().upper()

frase = f.replace(' ', '')
inverso = ''

for letra in range(len(frase)-1, -1, -1):
    inverso += frase[letra]

print('O inverso da frase "{}" é "{}"'.format(frase, inverso))
if frase == inverso:
    print('Temos um Palíndromo')
else:
    print('NÃO é um Palíndromo')