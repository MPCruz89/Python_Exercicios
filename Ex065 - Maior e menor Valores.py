from time import sleep
count = 0
soma = 0
maior = 0
menor = 0
resp = ''


while resp in 'Ss':
    n = int(input('Digite um número: '))
    count += 1
    soma += n
    if count == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()
    while resp not in 'SsNn':
        resp = str(input('OPÇÃO INVÁLIDA. Escolha entre [S/N]: : '))

print('ANALISANDO VALORES...')
sleep(1)
print('Você digitou {} números'.format(count))
print('Soma dos números = {}'.format(soma))
media = soma/count
print('Média dos números = {:.1f}'.format(media))
print('Maior número = {}'.format(maior))
print('Menor número = {}'.format(menor))