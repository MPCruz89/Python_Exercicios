#Funções estão ligadas a Rotina

def titulo(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)


#Programa principal
titulo('     OI     ')


a = 4
b = 5
s = a + b
print(s)

a = 8
b = 9
s = a + b
print(s)

a = 2
b = 1
s = a + b
print(s)

def soma(*valores): # Desempacotamento
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


#Programa principal
soma(4, 5)
soma(7, 2)
soma(3, 9, 5)

def contador(*num): # * = Vou receber parâmetros, mas não sei a quantidade (Desempacotamento)
    for v in num:
        print(f'{v} ', end='')
    print('FIM!')


#Programa principal "Contador"
contador(5, 7, 3, 1, 4)
contador(8, 4, 7)


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


#Programa principal "Dobra valores da lista"
valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)