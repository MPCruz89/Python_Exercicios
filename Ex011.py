l = float(input('Informe a largura da parede: '))
a = float(input('Informe a altura da parede: '))

area = l * a

print('Sua parede tem {:.2f}m de largura e {:.2f}m de altura, resultando em {:.2f}m².\nSerá necessário {:.2f}l de tinta'.format(l, a, area, area/2))
