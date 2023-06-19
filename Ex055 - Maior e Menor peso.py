menor = 0
maior = 0

for c in range(1, 6):
    peso = float(input('Informe o {}º peso.(Kg) '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso

        if peso < menor:
            menor = peso

print('O maior peso foi \033[34m{}Kg\033[m e o menor peso foi \033[31m{}Kg\033[m'.format(maior, menor))