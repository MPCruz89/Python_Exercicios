from math import sin, cos, tan, radians, degrees

a = float(input('Informe um ângulo: '))

print('Você informou o ângulo {}. O seno é {}, o cosseno  é {} e a tangente é {}.'.format(a, sin(degrees(a)), cos(degrees(a)), tan(degrees(a))))
