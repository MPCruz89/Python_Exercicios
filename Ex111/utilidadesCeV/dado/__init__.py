def leiaDinheiro(msg):
    ok = False
    preco = 0
    while True:
        n = str(input(msg)).replace(',', '.').strip()
        if n.isalpha() or n == '':
            print(f'\033[1;31mERRO!! "{n}" é um preço inválido\033[m')
        else:
            preco = float(n)
            ok = True
            break
        if ok:
            break
    return preco
