sal = float(input('Informe seu salário atual: R$'))

if sal > 1250:
    novo_sal = sal * 1.1
else:
    novo_sal = sal * 1.15

print('Seu salário era de \033[31mR${:.2f}\033[m, mas com o aumento passará a ser de \033[35mR${:.2f}\033[m.'.format(sal, novo_sal))