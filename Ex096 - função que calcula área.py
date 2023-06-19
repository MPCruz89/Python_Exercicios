print(' Controle de Terrenos')
print('-' * 22)

def area(a, b):
    area = a * b
    print(f'A área de um terreno de {a:.1f}x{b:.1f} é de {area:.1f}m²')


#Programa principal
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))

area(l, c)