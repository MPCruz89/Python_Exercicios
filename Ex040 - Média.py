n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))

m = (n1 + n2) / 2

if m < 5:
    print('Sua media foi de {}. Aluno \033[1;31mREPROVADO!\033[m'.format(m))
elif 5 <= m < 7:
    print('Sua media foi de {}. Aluno \033[1;34mEM RECUPERAÇÃO\033[m'.format(m))
else:
    print('Sua média foi de {}. Aluno \033[1;32mAPROVADO\033[m'.format(m))