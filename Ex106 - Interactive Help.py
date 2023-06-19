from time import sleep

while True:
    print('~' * 28)
    print(f'  SISTEMA DE AJUDA PyHELP')
    print('~' * 28)
    sleep(.3)
    opc = str(input('Função ou Biblioteca > '))
    if opc == 'fim':
        print('~' * 13)
        print(f'  ATÉ LOGO')
        print('~' * 13)
        break
    else:
        print('~' * (36 + (len(opc))))
        print(f'  Acessando o manual do comando "{opc}" ')
        print('~' * (36 + (len(opc))))
        sleep(1)
        help(opc)
        sleep(1)