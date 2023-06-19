from time import sleep

soma = 0
h_velho = 0
n_velho = ''
m_vinte = 0
for c in range(1, 5):
    nome = input('Informe o {}º nome: '.format(c))
    idade = int(input('Informe sua idade: '))
    soma += idade
    sexo = input('Informe o sexo [M/F]: ')
    print('='* 20)
    if idade > h_velho and sexo in 'Mm':
        h_velho = idade
        n_velho = nome
    if sexo in 'Ff' and idade < 20:
        m_vinte += 1

media = soma/4
print('ANALISANDO INFORMAÇÕES...')
print('='* 20)
sleep(1.5)
print('A media de idade do grupo é de \033[1;31m{:.1f}\033[m anos'.format(media))
print('O homem mais velho chama-se \033[34m{}\033[m e tem \033[34m{}\033[m anos'.format(n_velho, h_velho))
print('Existem \033[2;32m{}\033[m mulheres com menos de 20 anos.'.format(m_vinte))