def metade(v = 0, show = False):
    """
    -> Função para calcular a metade de um valor
    :param v: Parâmetro do valor informado
    :param show: Opção se irá mostrar o valor formatado ou não
    :return: Retorna a metade do valor informado
    """
    res = v / 2
    if show is False:
        return res
    else:
        return moeda(res)


def dobro(v = 0, show = False):
    """
    -> Função para calcular o dobro de um valor
    :param v: Parâmetro do valor informado
    :param show: Opção se irá mostrar o valor formatado ou não
    :return: Retorna o dobro do valor informado
    """

    res = v * 2
    if show is False:
        return res
    else:
        return moeda(res)


def aumento(v = 0, perc = 0, show = False):
    """
    -> Função para calcular o aumento em relação a taxa informada
    :param v: Parâmetro do valor informado
    :param perc: Parâmetro da taxa de aumento
    :param show: Opção se irá mostrar o valor formatado ou não
    :return: Retorna o valor aumentado de acordo com a taxa informada
    """

    res = v + (v * perc/100)
    if show is False:
        return res
    else:
        return moeda(res)


def diminuir(v = 0, perc = 0, show = False):
    """
    -> Função para calcular a diminuição do valor em relação a taxa informada
    :param v: Parâmetro do valor informado
    :param perc: Parâmetro da taxa de decréscimo
    :param show: Opção se irá mostrar o valor formatado ou não
    :return: Retorna o valor decrescido de acordo com a taxa informada
    """

    res = v - (v * perc/100)
    if show is False:
        return res
    else:
        return moeda(res)


def moeda(v=0, moeda='R$'):


    """
    -> Função para formatar a moeda
    :param v: Parâmetro do valor a ser formatado
    :param moeda: Parâmetro do tipo de moeda utilizado
    :return: Retorna o valor da moeda já formatado
    """
    return f'{moeda}{v:.2f}'.replace('.', ',')

