import urllib.request
from urllib import request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site pudim não está acessível no  momento')
else:
    print('Consegui acessar o site com sucesso')
    print(site.read())