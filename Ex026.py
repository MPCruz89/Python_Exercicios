frase = input('Digite uma frase qualquer: ').strip()

print('Quantas vezes aparece a letra a? {}'.format(frase.lower().count('a')))
print('Em qual posição ela aparece a primeira vez? {}'.format(frase.lower().find('a')+1))
print('Em qual posição ela aparece a última vez? {}'.format(frase.lower().rfind('a')+1))
