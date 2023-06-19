r1 = float(input('Informe o valor da reta 1: '))
r2 = float(input('Informe o valor da reta 2: '))
r3 = float(input('Informe o valor da reta 3: '))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('\033[1;32mÉ POSSÍVEL\033[m formar um triângulo!!')

    if r1 == r2 == r3:
        print('Será formado um triângulo \033[34mequilátero\033[m (todos os lados iguais)')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Será formado um triângulo \033[34misósceles\033[m (dois lados iguais)')
    else:
        print('Será formado um triângulo \033[34mescaleno\033[m (todos os lados diferentes)')

else:
    print('\033[1;31mNÃO\033[m é possível formar um triângulo')