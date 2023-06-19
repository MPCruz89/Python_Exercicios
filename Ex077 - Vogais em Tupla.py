
palavras = ('lapis', 'linguagem', 'python', 'curso', 'programacao', 'dinheiro', 'aprender', 'gratis', 'estudar')



for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra in 'aeiou':
            print('\033[34m',letra,'\033[m',end='')
