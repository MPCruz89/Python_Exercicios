nome = input('Informe seu nome completo: ').strip()

print(nome.upper())
print(nome.lower())
novo = nome.replace(' ', '')
div = nome.split()
print('Seu nome possui {} letras'.format(len(novo)))
print('Seu primeiro nome tem {} letras'.format(len(div[0])))
