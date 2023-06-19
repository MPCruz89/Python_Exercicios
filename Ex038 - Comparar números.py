n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))

if n1 > n2:
    print('O \033[1;33mprimeiro\033[m valor é maior')
elif n2 > n1:
    print('O \033[1;33msegundo\033[m valor é maior')
else:
    print('Os dois número são \033[1;33miguais\033[m')