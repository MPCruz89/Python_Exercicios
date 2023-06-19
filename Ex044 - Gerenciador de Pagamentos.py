
print('{:=^40}'.format('LOJAS MARCOS'))

valor = float(input('Informe o valor normal do produto: R$'))

print('''FORMAS DE PAGAMENTO
[ 1 ] Á Vista: Dinheiro ou Cheque
[ 2 ] Á Vista: Cartão
[ 3 ] Até 2X no Cartão
[ 4 ] 3X ou mais no Cartão''')

opcao = int(input('Informe a opção de pagamento: '))

if opcao == 1:
    print('Você terá 10% de desconto e irá pagar \033[32mR${:.2f}\033[m pelo produto'.format(valor * 0.9))
elif opcao == 2:
    print('Você terá 5% de desconto e irá pagar \033[32mR${:.2f}\033[m pelo produto'.format(valor * 0.95))
elif opcao == 3:
    print('Você irá pagar \033[34mR${:.2f}\033[m pelo produto'.format(valor))
elif opcao == 4:
    print('Você  terá um acréscimo de 20% e irá pagar \033[31mR${:.2f}\033[m'.format(valor * 1.20))
else:
    print('Opção Inválida de pagamento. Tente novamente!!')