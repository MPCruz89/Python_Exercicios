from random import randint
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10... Tente adivinhar!!')
print('-=-' * 20)

n_pc = randint(0, 10)
n_user = int(input('Em qual número eu pensei? '))
cont = 1

if n_user == n_pc:
    print('Você e o PC escolheram o número {}. PARABÉNS, VOCÊ GANHOU!!!'.format(n_pc))
    print('Você precisou de {} tentativa'.format(cont))
else:
    while n_user != n_pc:
        if n_user > n_pc:
            n_user = int(input('Menos...TENTE NOVAMENTE: '.format(n_user, n_pc)))
        else:
            n_user = int(input('Mais...TENTE NOVAMENTE: '.format(n_user, n_pc)))
        cont += 1
    print('Você e o PC escolheram o número {}. PARABÉNS, VOCÊ GANHOU!!!'.format(n_pc))
    print('Você precisou de {} tentativas'.format(cont))



'''print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5... Tente adivinhar!!')
print('-=-' * 20)

n_user = int(input('Em qual número eu pensei? '))
n_pc = randint(0, 5)

if n_user == n_pc:
    print('Você e o PC escolheram o número {}. PARABÉNS, VOCÊ GANHOU!!!'.format(n_pc))
else:
    print('Você escolheu o número {} e o PC, o número {}. VOCÊ PERDEU!!!'.format(n_user, n_pc))'''