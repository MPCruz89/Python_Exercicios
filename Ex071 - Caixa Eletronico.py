saque = int(input('Qual será o valor sacado? '))
notas50 = 0
notas20 = 0
notas10 = 0
notas1 = 0

while True:
    if saque % 50 == 0:
        notas50 = saque // 50
        print(f'Total de {notas50} cédulas de R$50')
        break
    else:
        notas50 = saque // 50
        resto = saque % 50
        if resto % 20 == 0:
            notas20 = resto // 20
            print(f'Total de {notas50} cédulas de R$50')
            print(f'Total de {notas20} cédulas de R$20')
            break
        else:
            if resto % 10 == 0:
                notas50 = saque // 50
                notas20 = resto // 20
                notas10 = ((resto % 20) // 10)
                print(f'Total de {notas50} cédulas de R$50')
                print(f'Total de {notas20} cédulas de R$20')
                print(f'Total de {notas10} cédulas de R$10')
                break
            else:
                if resto % 1 == 0:
                    notas50 = saque // 50
                    notas20 = resto // 20
                    notas10 = ((resto % 20) // 10)
                    notas1 = ((resto % 10) // 1)
                    print(f'Total de {notas50} cédulas de R$50')
                    print(f'Total de {notas20} cédulas de R$20')
                    print(f'Total de {notas10} cédulas de R$10')
                    print(f'Total de {notas1} cédulas de R$1')
                    break
