def votar(ano):
    from datetime import date
    idade = date.today().year - ano
    if 18 <= idade < 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'
    elif 16 <= idade < 18 or idade >= 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO NEGADO'


#Programa Principal
print('-' * 30)
nasc = int(input('Em que ano você nasceu? '))
print(votar(nasc))