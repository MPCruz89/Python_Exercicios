from time import sleep

def maior(*valores):
    print('-=' * 30)
    print('Analisando os valores passados...')
    for num in range(0, len(valores)):
        if num == 0:
            maior = valores[num]
        else:
            if valores[num] > maior:
                maior = valores[num]
        print(valores[num], end=' ',)
        sleep(.3)
    print(f'Foram informados {len(valores)} valores ao todo.')
    print(f'O maior valor informado foi {maior}')


maior(3, 4, 2)
maior(2, 5, 1, 7, 8, 4)
maior(6)
maior(6, 4, 7, 1)
maior(0)