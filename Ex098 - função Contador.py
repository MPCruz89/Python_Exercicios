from time import sleep

def contador():
    print('-=' * 20)
    print('Contagem de 1 a 10 de 1 em 1')
    for c in range (1, 11):
        print(c, end=' ')
        sleep(.3)
    print('FIM!')
    print('-=' * 20)
    print('Contagem de 10 até 0 de 2 em 2')
    for c in range(10, -1, -2):
        print(c, end=' ')
        sleep(.3)
    print('FIM!')
    print('-=' * 20)
    print('Agora é sua vez de personalizar a contagem!')
    a = int(input('Início: '))
    b = int(input('Fim: '))
    c = int(input('Passo: '))
    if c == 0:
        c = 1
    print('-=' * 20)
    if b > a and c > 0:
        print(f'Contagem de {a} até {b} de {c} em {c}')
        for cont in range(a, b+1, c):
            print(cont, end=' ')
            sleep(.3)
    if a > b:
        if c >= 0:
            print(f'Contagem de {a} até {b} de {c} em {c}')
            for cont in range(a, b-1, -c):
                print(cont, end=' ')
                sleep(.3)
        else:
            print(f'Contagem de {a} até {b} de {c*(-1)} em {c*(-1)}')
            for cont in range(a, b-1, c):
                print(cont, end=' ')
                sleep(.3)
    print('FIM!')

contador()
