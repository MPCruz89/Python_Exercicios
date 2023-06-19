print('\033[2;34m-='*12)
print('APROVADOR DE EMPRÉSTIMO')
print('-='*12)
print('\033[m')

v_casa = int(input('Qual o valor da casa? R$'))
s = float(input('Qual seu salário? R$'))
anos = int(input('Em quantos anos você vai pagar o empréstimo? '))

meses = anos * 12
p_mensal = v_casa/meses
sal_limite = s * 0.30

if sal_limite >= p_mensal:
    print('Seu limite de crédito é de \033[34mR${:.2f}\033[m e a prestação da casa é de R${:.2f} em {} meses. \033[1;32mEMPRÉSTIMO APROVADO!!\033[m'.format(sal_limite, p_mensal, meses))
else:
    print('Seu limite de crédito é de \033[34mR${:.2f}\033[m e a prestação da casa é de R${:.2f} em {} meses. \033[1;31mEMPRÉSTIMO REPROVADO!!\033[m'.format(sal_limite, p_mensal, meses))