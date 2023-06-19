def metade(v):
    res = v / 2
    return res


def dobro(v):
    res = v * 2
    return res


def aumento(v, perc):
    res = v * ((perc / 100)+1)
    return res


def diminuir(v, perc):
    res = v - ((v / 100) * perc)
    return res