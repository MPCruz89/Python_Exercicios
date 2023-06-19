from random import randint

print('-=' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=' * 15)

jogador = 0
computador = 0
escolha = ''
soma = 0
cont = 0

while True:
    jogador = int(input('Escolha um número: '))
    escolha = str(input('Par ou Ímpar? [P/I]')).strip().upper()
    while escolha not in 'PI':
        escolha = str(input('VALOR INVÁLIDO!! Escolha entre Par ou Ímpar? [P/I]')).strip().upper()
    print('-' * 30)
    computador = randint(0,10)
    soma = jogador + computador
    if soma % 2 == 0:
        print(f'Você jogou {jogador} e o PC jogou {computador}. Total de {soma}. DEU PAR')
    else:
        print(f'Você jogou {jogador} e o PC jogou {computador}. Total de {soma}. DEU ÍMPAR')
    print('-' * 30)
    if (escolha == 'I' and soma % 2 != 0) or (escolha == 'P' and soma % 2 == 0):
        print('VOCÊ VENCEU!!!')
        cont += 1
    else:
        print(f'VOCÊ PERDEU!!! Você venceu {cont} vezes.')
        break
    print('Vamos jogar novamente...')
    print('-=' * 15)
