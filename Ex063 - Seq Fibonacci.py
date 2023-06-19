n = int(input('Quantos números da Seq. Fibonacci você quer ver? '))

count = 1
soma = 1
n1 = 0
n2 = 1
print('{}'.format(n1), end=' → ')
print('{}'.format(n2), end=' → ')

while count <= n-2:
    soma = n1 + n2
    n2 = soma
    n1 = soma - n1
    print('{}'.format(soma), end=' → ')
    count +=1
print('ACABOU!!')
