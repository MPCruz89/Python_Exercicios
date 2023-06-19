from time import sleep
n = int(input('Informe um número para calcular a tabuada: '))

print('{:=^15}'.format('TABUADA'))
for c in range (1, 11):
    print('{}  x {:2} = {:2}'.format(n, c, n*c))
    sleep(.3)