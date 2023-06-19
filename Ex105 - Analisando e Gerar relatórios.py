def notas(*notas, sit = False):
    """
    -> Função para analisar notas e situações de vários alunos
    :param notas: Uma ou mais notas de vários alunos (aceita várias)
    :param sit: Valor adicional, se deve ou não mostrar a situaçãod do aluno
    :return: Dicionário com várias informações sobre a situação da turma.
    """

    dic = {}
    maior = menor = soma = media = 0
    dic['total'] = len(notas)
    dic['maior'] = max(notas)
    dic['menor'] = min(notas)
    dic['média'] = sum(notas) / len(notas)
    if sit:
        if dic['média'] < 5:
            dic['situação'] = 'RUIM'
        elif dic['média'] < 7:
            dic['situação'] = 'RAZOÁVEL'
        else:
            dic['situação'] = 'BOA'
    return dic


#Programa Principal
resp = notas(3.5, 9, 6.5, 7, 9, sit=True)
print(resp)

help(notas)