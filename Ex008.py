m = float(input('Digite o valor em metros: '))

cm = m * 100
mm = m * 1000

print('Você informou o valor de {:.2f}m, que equivale a {:.2f}cm ou a {:.2f}mm'.format(m, cm, mm))
