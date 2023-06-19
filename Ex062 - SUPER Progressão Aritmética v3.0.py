print('='*30)
print('{:^30}'.format('10 TERMOS DE UMA PA'))
print('='*30)

primeiro = int(input('Informe o primeiro termo da PA: '))
razao = int(input('Informe a razão da PA: '))
cont = 1
valor = primeiro + razao

print('{}'.format(primeiro), end=' → ')
while cont < 10:
    print('{}'.format(valor), end=' → ')
    valor += razao
    cont += 1
r = int(input('\nQuer mostrar mais quantos termos? '))
cont = 0
if r != 0:
    while cont <= r-1:
        print('{}'.format(valor), end=' → ')
        valor += razao
        cont += 1
        if cont == r:
            cont = 0
            r = int(input('\nQuer mostrar mais quantos termos? '))
print('ACABOU!!')