#Interactive Help
#help(input)

#Docstrings
def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: Início da contagem
    :param f: Fim da contagem
    :param p: Passo da contagem
    :return: sem retorno
    Função criada por Marcos Paulo
    """

    '''c = i
    while c <= f:
        print(f'{c}', end=' ')
        c+=p
    print('FIM!')


help(contador)'''

#Parâmetros opcionais(informar ou não a variável)
'''
def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}')

somar(3, 2, 5)
somar(8, 4)
somar()

help(print())'''

#Escopo de variáveis
'''def teste():
    x = 8 #x é uma variável local. Não vai funcionar no programa principal
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')

n = 2
print(f'No programa principal, n vale {n}')
teste()
print(f'No programa principal, x vale {x}')'''

'''def funcao():
    n1 = 4
    print(f'N1 dentro vale {n1}')


n1 = 2
funcao()
print(f'N1 fora vale {n1}')

def teste(b):
    #global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a = 5
teste(a)
print(f'A fora vale {a}')'''

#RETORNO DE VALORES
'''def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = (somar(3, 2, 5))
r2 = (somar(2, 4))
r3 = (somar(1, 3, 1))

print(f'As somas deram {r1}, {r2} e {r3}')'''

def fatorial(n=1):
    f = 1
    for c in range(n, 0, -1):
        f *= c
    return f


f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()

print(f'Os resultados são {f1}, {f2} e {f3}')


def ParouImpar(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
if ParouImpar(num):
    print('É par!')
else:
    print('Não é par!')
