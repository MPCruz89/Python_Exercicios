n = 0
c = 1
while True:
    c = 1
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*30)
    if n < 0:
        break
    while c <= 10:
        print(f'{n} X {c} = {n * c}')
        c += 1
    print('-'*30)
print('PROGRAMA ENCERRADO!!')