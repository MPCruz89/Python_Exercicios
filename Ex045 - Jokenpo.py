from random import choice
from time import sleep

print('Vamos jogar JO-KEN-PO?')
opc_US = input('Escolha sua opção: PEDRA, PAPEL ou TESOURA: ').strip().lower()
print('JO')
sleep(.6)
print('KEN')
sleep(.6)
print('PO')
sleep(.6)

print('-='*10)

lista = ['PEDRA','PAPEL', 'TESOURA']

opc_PC = choice(lista).strip().lower()


if (opc_PC == 'pedra' and opc_US == 'pedra') or (opc_PC == 'papel' and opc_US == 'papel') or (opc_PC == 'tesoura' and opc_US == 'tesoura'):
    print('EMPATOU!! Ambos escolheram \033[33m{}\033[m'.format(opc_PC))
elif (opc_PC == 'pedra' and opc_US == 'tesoura') or (opc_PC == 'papel' and opc_US == 'pedra') or (opc_PC == 'tesoura' and opc_US == 'papel'):
    print('O PC escolheu \033[33m{}\033[m \nVocê escolheu \033[33m{}\033[m. \nVOCÊ PERDEU!!'.format(opc_PC, opc_US))
else:
    print('O PC escolheu \033[33m{}\033[m \nVocê escolheu \033[33m{}\033[m. \nPARABÉNS, VOCÊ GANHOU!!'.format(opc_PC, opc_US))
print('-='*10)