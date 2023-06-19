p = float(input('informe o preço do produto: '))

p_des = p * 0.95

print('O valor do produto é R${:.2f}, mas com desconto de 5% passa a ser de R${:.2f}'.format(p, p_des))
