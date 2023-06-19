
def fatorial(n, show=False):
    """
    -> Calcular o fatorial de um número
    :param n: O número a ser calculado
    :param show: Opcional: Mostrar ou não a conta
    :return: O valor do fatorial de um número
    """
    f = 1
    for num in range(n, 0, -1):
        if show:
            if num > 1:
                print(f'{num} X', end=' ')
            else:
                print(f'{num} =', end=' ')
        f *= num
    return f


print('-' * 30)
num = int(input('Quer saber o fatorial de qual número? '))
print(fatorial(num, show=True))