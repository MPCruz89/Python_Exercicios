from random import randint
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5... Tente adivinhar!!')
print('-=-' * 20)

n_user = int(input('Em qual número eu pensei? '))
n_pc = randint(0, 5)

if n_user == n_pc:
    print('Você e o PC escolheram o número {}. PARABÉNS, VOCÊ GANHOU!!!'.format(n_pc))
else:
    print('Você escolheu o número {} e o PC, o número {}. VOCÊ PERDEU!!!'.format(n_user, n_pc))
