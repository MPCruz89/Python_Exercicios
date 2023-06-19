print('{:=^40}'.format('MÁQUINA DE CALCULAR'))

n1 = int(input('Informe o primeiro valor: '))
n2 = int(input('Informe o segundo valor: '))

opcao = 0

while opcao != 5:
    print('-=' * 20)
    print('[ 1 ] SOMAR')
    print('[ 2 ] MULTIPLICAR')
    print('[ 3 ] MAIOR')
    print('[ 4 ] NOVOS NÚMEROS')
    print('[ 5 ] SAIR DO PROGRAMA')
    opcao = int(input('Escolha uma OPÇÃO: '))

    if opcao == 1:
        print('A soma dos valores {} e {} é {}'.format(n1, n2, n1 + n2))
        print('-=' * 20)
        #opcao = int(input('Escolha uma OPÇÃO: '))
    elif opcao == 2:
        print('O produtos entre os valores {} e {} é {}'.format(n1, n2, n1 * n2))
        print('-=' * 20)
        #opcao = int(input('Escolha uma OPÇÃO: '))
    elif opcao == 3:
        if n1 > n2:
            print('{} é o MAIOR número'.format(n1))
            print('-=' * 20)
        elif n2 > n1:
            print('{} é o MAIOR número'.format(n2))
            print('-=' * 20)
        else:
            print('Ambos os valores são iguais!!')
            print('-=' * 20)
        #opcao = int(input('Escolha uma OPÇÃO: '))
    elif opcao == 4:
        print('-=' * 20)
        n1 = int(input('Escolha outro número para o primeiro valor: '))
        n2 = int(input('Escoolha outro número para o segundo valor: '))
        #opcao = int(input('Escolha uma OPÇÃO: '))
    else:
        opcao = int(input('Opção Inválida!! Escolha uma opção entre 1 e 5: '))
print('PROGRAMA FINALIZADO!!')