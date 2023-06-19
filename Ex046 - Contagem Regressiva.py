from time import sleep

print('{:=^30}'.format('CONTAGEM REGRESSIVA'))
for c in range(10, -1, -1):
    print(c)
    sleep(0.5)
print('\033[1;34mFELIZ ANO NOVO!!!!\033[m')