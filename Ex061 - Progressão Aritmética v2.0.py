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
print('ACABOU!!')



'''print('='*30)
print('{:^30}'.format('10 TERMOS DE UMA PA'))
print('='*30)

primeiro = int(input('Informe o primeiro termo da PA: '))
razao = int(input('Informe a razão da PA: '))
decimo = primeiro + (10-1) * razao

for c in range(primeiro, decimo + razao, razao):
    print('{}'.format(c), end=' → ')
print('ACABOU!!')'''