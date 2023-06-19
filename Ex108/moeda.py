def metade(v = 0):
    res = v / 2
    return res


def dobro(v = 0):
    res = v * 2
    return res


def aumento(v = 0, perc = 0):
    res = v + (v * perc/100)
    return res


def diminuir(v = 0, perc = 0):
    res = v - (v * perc/100)
    return res


def moeda(v=0, moeda='R$'):
    return f'{moeda}{v:.2f}'.replace('.', ',')

