numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

n = int(input('Digite um número entre 0 e 20: '))
if n < 0 or n > 20:
    while True:
        n = int(input('Tente novamente. Digite um número entre 0 e 20: '))
        if 0 <= n <= 20:
            break

for c in range(0, len(numeros)):
    if n == c:
        print(f'Você digitou o número {numeros[c]}')



